import re
def generic_getmode(arg1, arg2):
    if arg1[1] == "m" and arg2[1] == "m":
        return 1
    elif arg1[1] == "m" and arg2[1] == "l":
        return 2
    return 3

def tp(a):
    if isinstance(a, tuple):
        return hex(a[0]).replace("0x", "").zfill(2)
    return hex(a).replace("0x", "").zfill(2)
def generic_gen_opcode(op, arg1, arg2, mode):
        return op + tp(arg1) + tp(arg2) + tp(mode)

def decode_hex_mem(a):
    if "m0x" in a:
        return int(a.replace("m0x", ""), 16)
    else:
        return int(a.replace("m", ""), 10)

def decode_hex(a):
    if "0x" in a:
        return int(a.replace("0x", ""), 16)
    else:
        return int(a, 10)

def ret_mem(a):
        if "m" in a:
            return (decode_hex_mem(a), "m")
        else:
            return (decode_hex(a), "l")

class Opcode():
    def __init__(self, opcode, arg1, arg2, f_getmode, f_gen_opcode):
        self.opcode = operations_dict[opcode][0]
        self.arg1 = arg1
        self.arg2 = arg2
        self.f_getmode = f_getmode
        self.f_gen_opcode = f_gen_opcode
    
    def generate(self):
        opcode = self.opcode
        arg1 = ret_mem(self.arg1)
        arg2 = ret_mem(self.arg2)
        mode = self.f_getmode(arg1, arg2)
        return self.f_gen_opcode(opcode, arg1, arg2, mode)

class op_generic(Opcode):
    def __init__(self, arr):
        super().__init__(arr[0], arr[1], arr[2], generic_getmode,
            generic_gen_opcode)

class op_inc_dec(Opcode):
    def __init__(self, arr):
        super().__init__(arr[0], arr[1], "00",
            lambda x, y: 1,
            lambda o, a1, a2, m: o + tp(a1) + tp(m) + tp(0)
        )

class op_concat(Opcode):
    def __init__(self, arr):
        super().__init__(arr[0], arr[1], "00",
            lambda x, y: 0,
            lambda o, a1, a2, m: o + hex(a1).replace("0x", "").zfill(6)
        )

class op_one_arg(Opcode):
    def __init__(self, arr):
        super().__init__(arr[0], arr[1], "00",
            lambda x, y: 1 if x[1] == "m" else 2,
            lambda o, a1, a2, m: o + tp(a1) + tp(m) + "00"
        )

class op_one_arg_no_mode(Opcode):
    def __init__(self, arr):
        super().__init__(arr[0], arr[1], "00",
            lambda x, y: 1,
            lambda o, a1, a2, m: o + tp(a1) + "0000"
        )

class op_no_mode(Opcode):
    def __init__(self, arr):
        super().__init__(arr[0], arr[1], "00",
            lambda x, y: 1,
            lambda o, a1, a2, m: o + tp(a1) + tp(a2) + "00"
        )

operations_dict = {
    "mov": ("00", op_generic),
    "inc": ("01", op_inc_dec),
    "dec": ("02", op_inc_dec),
    "add": ("03", op_generic),
    "sub": ("04", op_generic),
    "mul": ("05", op_generic),
    "div": ("06", op_generic),
    "cmp": ("07", op_generic),
    "jmp": ("08", op_concat),
    "jmpz": ("09", op_concat),
    "jmpnz": ("0a", op_concat),
    "write": ("0b", op_one_arg),
    "read": ("0c", op_one_arg_no_mode),
    "hlt": ("0d", op_one_arg),
    "store": ("0e", op_concat),
    "load": ("0f", op_concat),
    "xor": ("10", op_generic),
    "and": ("11", op_generic),
    "or": ("12", op_generic),
    "not": ("13", op_generic),
    "bsl": ("14", op_generic),
    "bsr": ("15", op_generic),
    "movl": ("16", op_concat),
    "lfa": ("17", op_no_mode),
    "lta": ("18", op_generic),
}

def generate_bin(data):
    splits = ["\n", ";"]
    temp = re.split(str("|".join(splits)), data)
    ast = [0 for i in range(len(temp))]
    for i in range(len(temp)):
        ast[i] = re.split(str("|".join([",", " ", "\t"])), temp[i])
        ast[i] = [elem for elem in ast[i] if elem.strip()]
    ast = [elem for elem in ast if elem]
    final_output = ""
    count = 0
    for elem in ast:
        tmp = operations_dict[elem[0]][1](elem)
        print(elem)
        ast[count] = tmp.generate()
        count += 1
        print(tmp.generate())