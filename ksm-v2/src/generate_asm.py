from dataclasses import dataclass
import re
import cursed
@dataclass
class status():
    is_in_raw: bool = 0
    rcx: bool = 0
    register_list = ("r9", "r10", "r11", "r12", "r13", "r14", "r15")
    ue = ("r9", "r10", "r11", "r12", "r13", "r14", "r15", "rax","rbx","rcx","rdx","rsi","rdi","rsp","rbp")
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
# Helper function that just returns some stuff we need, eg memory allocation
def td(n: str) -> int:
    if "m" in n and "x" in n:
        return int(n[1:len(n)], 16)
    elif "m" in n:
        return int(n[1:len(n)])
    elif "x" in n:
        return int(n, 16)
    else:
        return int(n)
def mov_arg_to_reg(a: str, reg: str, ue: bool = False) -> str:
    if a in status.register_list or ue and a in status.ue:
        if "[" in a:
            return f"   mov qword {reg}, [rcx + {a[1:-1]} * 8]\n"
        else:
            return f"   mov qword {reg}, {a}\n"
    elif "m" in a:
        if "[" in a:
            fin = f"   mov qword rbx, [rcx + {a[1:-1]} * 8]\n"
            return fin + f"    mov qword {reg}, [rcx + rbx * 8]\n"
        else:
            return f"   mov qword {reg}, [rcx + {td(a)} * 8]\n"
    else:
        if "[" in a:
            return f"   mov qword {reg}, [rcx + {td(a[1:-1])} * 8]\n"
        else:
            return f"   mov qword {reg}, {td(a)}\n"

def mov_reg_from_arg(a: str, reg: str, ue: bool = False) -> str:
    print(a, reg, ue)
    if a in status.register_list or ue and a in status.ue:
        return f"   mov qword {a}, {reg}\n"
    elif "m" in a:
        return f"   mov qword [rcx + {td(a)} * 8], {reg}\n"
    else:
        return f"   mov qword {td(a)}, {reg}\n"

def gen_mov(a1: str, a2: str, ue: bool = False) -> str:
    fin = ""
    # a2 is src. a1 is dest.
    fin += mov_arg_to_reg(a2, "rax", ue)
    fin += mov_reg_from_arg(a1, "rax", ue)
    return fin

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

def gen_math(a1: str, a2: str, op: str) -> str:
    fin = ""
    # a2 is src. a1 is dest.
    fin += mov_arg_to_reg(a2, "rax")
    fin += mov_arg_to_reg(a1, "rbx")
    fin += f"   {op} rax, rbx\n"
    fin += mov_reg_from_arg(a1, "rax")
    return fin

def gen_cmp(a1: str, a2: str) -> str:
    fin = ""
    # a2 is src. a1 is dest.
    fin += mov_arg_to_reg(a2, "rax")
    fin += mov_arg_to_reg(a1, "rbx")
    fin += f"   cmp rax, rbx\n"
    return fin

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
def gen(stat: status, tok: str) -> str:
    tok = re.split("\\s+(?![^\\[]*\\])", tok)
    ret = ""

    if status.is_in_raw:
        if tok[0] == "{":
            # the { doesn't actually do anything, just looks nice
            return (0, "")
        if tok[0] == "}":
            # End of raw asm segment
            status.is_in_raw = False
            return (0, "\n\n; End of raw_asm segment\n\n")
        # Load a value from ksm's memory
        # yes, this is just renamed mov
        if tok[0] == "ksm_load":
            return (0, "\n" + gen_ksm_raw_mov(tok[1], tok[2]))
        # Store into ksm's memory
        # yes, this is the same as load
        if tok[0] == "ksm_store":
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
        ret += "mov qword rcx, [pointer]\n"
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
    elif tok[0] in ("pop", "peek", "push"):
        ret += gen_stack(tok[1], tok[0])
    elif tok[0] in ("jmp", "je", "jne", "jg", "jl"):
        # jumps are already correct nasm syntax ( i wonder why... )
        ret += " ".join(tok) + "\n"
    else:
        # Could be a lable, could be some random stuff, so we just print it
        ret += " ".join(tok) + "\n"
    a, b, c = cursed.evil(tok)
    return (0, "\n" + ret + f'; {a} {b} {c}\n\n')