d = { # Number of args for each op
    "mov": 2,
    "inc": 1,
    "dec": 1,
    "add": 2,
    "sub": 2,
    "mul": 2,
    "div": 2,
    "cmp": 2,
    "jmp": 1,
    "jmpz": 1,
    "jmpnz": 1,
    "write": 1,
    "read": 1,
    "hlt": 1,
    "store": 1,
    "load": 1,
    "xor": 2,
    "and": 2,
    "or": 2,
    "not": 1,
    "bsl": 2,
    "bsr": 2,
    "movl": 1,
    "lfa": 2,
    "lta": 2,
}
jmps = [
    "08",
    "09",
    "0a",
]
k = [
        [ # Class 0: Lable
            "jmp",
            "jmpz",
            "jmpnz",
        ],
        [ # Class 1: Mem loc
            "inc",
            "dec",
            "read",
        ],
        [ # Class 2: Expandable
            "store",
            "load",
            "movl"
        ],
        [ # Class 3: One arg
            "hlt",
            "not",
            "write",
        ],
        [ # Class 4: Two args, no mode
            "lfa"
        ],
]
opd = { # OP code to literal
    "mov": 0x0,
    "inc": 0x1,
    "dec": 0x2,
    "add": 0x3,
    "sub": 0x4,
    "mul": 0x5,
    "div": 0x6,
    "cmp": 0x7,
    "jmp": 0x8,
    "jmpz": 0x9,
    "jmpnz": 0xa,
    "write": 0xb,
    "read": 0xc,
    "hlt": 0xd,
    "store": 0xe,
    "load": 0xf,
    "xor": 0x10,
    "and": 0x11,
    "or": 0x12,
    "not": 0x13,
    "bsl": 0x14,
    "bsr": 0x15,
    "movl": 0x16,
    "lfa": 0x17,
    "lta": 0x18,
}
