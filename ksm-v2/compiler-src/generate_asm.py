from dataclasses import dataclass
import re
import cursed
@dataclass
class status_t():
    is_in_raw: bool = 0
    rcx: bool = 0
    register_list = ("r9", "r10", "r11", "r12", "r13", "r14", "r15")
    # Stands for Unrestriced Extension
    ue = ("r9", "r10", "r11", "r12", "r13", "r14", "r15", "rax","rbx","rcx","rdx","rsi","rdi","rsp","rbp")
    strings = {}
    inc = 0
# Helper function that just returns some stuff we need, eg memory allocation
def prelude(k: int) -> str:
    return f"""
bits 64
section .data
    pointer dq 1
    argv dq 1
    argc dq 1
section .text
    global main
    extern malloc
    extern print_int
    extern print_hex
    extern print_string
    extern print_newline
    extern open_file
.newline:
    .string ""
main:
    mov qword [argc], rdi
    mov qword [argv], rsi
    mov rax, {k}
    mov rbx, 8
    imul rax, rbx
    mov rdi, rax
    call malloc
    mov qword [pointer], rax
    mov qword rcx, [pointer]
; end prelude
"""

# Converts a ksm memory loc or number into decimal
def td(n: str) -> int:
    if "m" in n and "x" in n:
        return int(n[1:len(n)], 16)
    elif "m" in n:
        return int(n[1:len(n)])
    elif "x" in n:
        return int(n, 16)
    else:
        return int(n)

# Moves first argument into given register. `ue` lets it set to any register, not just KSM allowed registers.
def mov_arg_to_reg(a: str, reg: str, ue: bool = False) -> str:
    if a in status_t.register_list or ue and a in status_t.ue:
        if "[" in a:
            return f"   mov qword {reg}, [rcx + {a[1:-1]} * 8]\n"
        else:
            return f"   mov qword {reg}, {a}\n"
    elif "m" in a:
        if "[" in a:
            fin = f"   mov qword rbx, [rcx + {a[2:-1]} * 8]\n"
            return fin + f"   mov qword {reg}, [rcx + rbx * 8]\n"
        else:
            return f"   mov qword {reg}, [rcx + {td(a)} * 8]\n"
    else:
        if "[" in a:
            return f"   mov qword {reg}, [rcx + {td(a[1:-1])} * 8]\n"
        else:
            return f"   mov qword {reg}, {td(a)}\n"

# Moves from reg into first argument. See `ue` above.
def mov_reg_from_arg(a: str, reg: str, ue: bool = False) -> str:
    print(a, reg, ue)
    if a in status_t.register_list or ue and a in status_t.ue:
        return f"   mov qword {a}, {reg}\n"
    elif "m" in a:
        return f"   mov qword [rcx + {td(a)} * 8], {reg}\n"
    else:
        return f"   mov qword {td(a)}, {reg}\n"

# Generates move instructions
def gen_mov(a1: str, a2: str, ue: bool = False) -> str:
    fin = ""
    # a2 is src. a1 is dest.
    fin += mov_arg_to_reg(a2, "rax", ue)
    fin += mov_reg_from_arg(a1, "rax", ue)
    return fin

# Raw mov for use in `raw_asm` section. Accounts for allowance of use of `rax`.
def gen_ksm_raw_mov(a1: str, a2: str) -> str:
    fin = ""
    if a1 == "rax":
        tmp = "rbx"
    else:
        tmp = "rax"
    fin += f"   push {tmp}\n"
    fin += mov_arg_to_reg(a2, tmp, True)
    fin += mov_reg_from_arg(a1, tmp, True)
    fin += f"   pop {tmp}"
    return fin

# Generate math instruction
def gen_math(a1: str, a2: str, op: str) -> str:
    fin = ""
    # a2 is src. a1 is dest.
    fin += mov_arg_to_reg(a2, "rax")
    fin += mov_arg_to_reg(a1, "rbx")
    fin += f"   {op} rax, rbx\n"
    fin += mov_reg_from_arg(a1, "rax")
    return fin

# Generate compare instruction
def gen_cmp(a1: str, a2: str) -> str:
    fin = ""
    # a2 is src. a1 is dest.
    fin += mov_arg_to_reg(a2, "rax")
    fin += mov_arg_to_reg(a1, "rbx")
    fin += f"   cmp rax, rbx\n"
    return fin

# Generate division or modulo instruction
def gen_divmod(a1: str, a2: str, m: int) -> str:
    fin = ""
    # a2 is src. a1 is dest. m decides whether to divide or modulo
    fin += mov_arg_to_reg(a2, "rax")
    fin += mov_arg_to_reg(a1, "rbx")
    fin += f"   idiv rax, rbx\n"
    if m == 1:
        reg = "rax"
    else:
        reg = "rdx"
    fin += mov_reg_from_arg(a1, reg)
    return fin

# Generate stack instruction
def gen_stack(a1: str, m: str) -> str:
    fin = ""
    if m == "push":
        fin += mov_arg_to_reg(a1, "rax")
        fin += f"   push rax\n"
    elif m == "pop":
        fin += f"   pop rax\n"
        fin += gen_mov(a1, "rax", True)
    elif m == "peek":
        fin += f"   pop rax\n"
        fin += gen_mov(a1, "rax", True)
        fin += f"   push rax\n"
    return fin

# Generate halt
def gen_hlt(a1: str) -> str:
    fin = ""
    fin += mov_arg_to_reg(a1, "rdi")
    fin += f"   mov qword rax, 60\n"
    fin += f"   syscall\n"
    return fin
# These two functions are needed because three of the user registers we have defined, r9-11
# are technically scratch registers and do not need to stay their current values
def pre_syscall():
    fin = ""
    fin += "   push r9\n"
    fin += "   push r10\n"
    fin += "   push r11\n"
    return fin

def post_syscall():
    fin = ""
    fin += "   pop r11\n"
    fin += "   pop r10\n"
    fin += "   pop r9\n"
    return fin

# Generate interger print
def gen_print_int(st: status_t, a1: str, print: str) -> str:
    fin = ""
    fin += pre_syscall()
    fin += mov_arg_to_reg(a1, "rdi")
    fin += f"   call {print}\n"
    fin += post_syscall()
    st.rcx = 1
    return fin


# Print a string
def gen_print_string(st: status_t, a1: str) -> str:
    fin = ""
    fin += pre_syscall()
    better_a1 = "_".join(a1.split(" ")) + "__KSM_INTERNAL"
    # If we don't already have the string, make it
    if better_a1 not in st.strings:
        st.strings[better_a1] = better_a1
        fin += f"._{better_a1}_:\n"
        fin += f'   .string "{a1}"\n'
        fin += f"___{st.inc}___:\n"
        st.inc += 1
    fin += f"   mov qword rdi, ._{better_a1}_\n"
    fin += f"   call print_string\n"
    fin += post_syscall()
    st.rcx = 1
    return fin


# Print a newline
def gen_print_newline(st: status_t) -> str:
    fin = ""
    fin += pre_syscall()
    fin += f"   call print_newline\n"
    fin += post_syscall()
    st.rcx = 1
    return fin

# Opens a file
def gen_open_file(st: status_t, a1: str, a2: str) -> str:
    fin = ""
    fin += pre_syscall()
    fin += f"   mov qword rdi, argv\n"
    fin += mov_arg_to_reg(a2, "rsi")
    fin += f"   call open_file\n"
    fin += mov_reg_from_arg(a1, "rax")
    fin += post_syscall()
    st.rcx = 1
    return fin


# Generate a token
def gen(status: status_t, tok: str) -> str:
    tok = re.split("\\s+(?![^\\[]*\\])", tok)
    ret = ""

    if status.is_in_raw:
        if tok[0] == "{":
            # the { doesn't actually do anything, just looks nice
            return (0, "")
        if tok[0] == "}":
            # End of raw asm segment
            status.is_in_raw = False
            status.rcx = 1
            return (0, "\n\n; End of raw_asm segment\n\n")
        # Load / store a value from ksm's memory
        if tok[0] in ("ksm_load", "ksm_store"):
            return (0, "\n" + gen_ksm_raw_mov(tok[1], tok[2]))
        return (0, "   " + " ".join(tok) + "\n")
    else:
        if tok[0] == "raw_asm":
            status.is_in_raw = True
            return (0, "\n\n; Start of raw_asm segment\n")
    ret = ""
    normal_ret = 1
    # rcx has been modified
    if status.rcx:
        ret += f"   mov qword rcx, [pointer]\n"
        status.rcx = 0
    # regular instructions
    if tok[0] == "mov":
        ret += gen_mov(tok[1], tok[2])
    elif tok[0] == "add":
        ret += gen_math(tok[1], tok[2], "add")
    elif tok[0] == "sub":
        ret += gen_math(tok[1], tok[2], "sub")
    elif tok[0] == "mul":
        ret += gen_math(tok[1], tok[2], "imul")
    elif tok[0] == "shl":
        ret += gen_math(tok[1], tok[2], "shl")
    elif tok[0] == "shr":
        ret += gen_math(tok[1], tok[2], "shr")
    elif tok[0] == "div":
        ret += gen_divmod(tok[1], tok[2], 1)
    elif tok[0] == "mod":
        ret += gen_divmod(tok[1], tok[2], 0)
    elif tok[0] == "cmp":
        ret += gen_cmp(tok[1], tok[2])
    elif tok[0] == "hlt":
        ret += gen_hlt(tok[1])
    elif tok[0] == "open_file":
        ret += gen_open_file(status, tok[1], tok[2])
    elif tok[0] == "print_string":
        # TLDR: This, in order: Joins the remaining tokens that were split earlier, 
        # removes the first one, which is the command, then removes the first and last char
        # which should always be the quotes around the string.
        tok = [tok[0], " ".join(tok[1:len(tok)])[1:-1]]
        ret += gen_print_string(status, tok[1])
    elif tok[0] == "print_newline":
        ret += gen_print_newline(status)
    elif tok[0] in ("pop", "peek", "push"):
        ret += gen_stack(tok[1], tok[0])
    elif tok[0] in ("print_int", "print_hex"):
        ret += gen_print_int(status, tok[1], tok[0])
    elif tok[0] in ("jmp", "je", "jne", "jg", "jl"):
        # jumps are already correct asm syntax ( i wonder why... )
        ret += " ".join(tok) + "\n"
    else:
        # Could be a lable, could be some random stuff, so we just print it
        ret += " ".join(tok) + "\n"
    
    # It's more fun this way.
    a, b, c = cursed.evil(tok)
    return (0, "\n" + ret + f'; {a} {b} {c}\n\n')