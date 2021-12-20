import ast
import re
import dict_ksm # This contains the info needed for ksm

lable_iter_dict = {}
lable_iter = 0
def hexfix(mhex):
    # Fix literals like "m0x91" into proper hex numbers, with an additional
    # bit for if it's a memory location
    if ":" in mhex:
        return (mhex, 0)
    if mhex[0].lower() == "m":
        ismem = 1
    else:
        ismem = 0
    mhex = mhex.replace("m", "")
    if "x" in mhex:
        return (int(mhex, 16), ismem)
    return (int(mhex), ismem)

def getmode(arg1, arg2):
    # Return a mode, based on the mode table
    if arg1 and arg2:
        return 1
    if arg1 and not arg2:
        return 2
    if not arg1 and not arg2:
        return 3
    raise Error("Invalid mode")

def assemble_op(op, arg1, arg2, mode):
    # Assemble an opcode.
    global lable_iter_dict
    global lable_iter
    k = dict_ksm.k
    if op in k[0]: # Using a lable
        if arg1 in lable_iter_dict:
            pass
        else:
            lable_iter_dict[arg1] = hex(lable_iter).replace("0x", "").zfill(6)
            lable_iter += 1
        return op + lable_iter_dict[arg1]
    if op in k[1]:
        return op + arg1.zfill(2) + "".zfill(4)
    if op in k[2]:
        return op + hex(int(arg1)).replace("0x", "").zfill(6)
class codegenerator():
    def __init__(self, tok_mast):
        self.ast = tok_mast
        self.lablere = re.compile("^[^\:]+:")
    def gencode_ksm(self):
        mast = self.ast.get_tok()
        i = 1
        for k in mast:
            op = k[0]
            op = str(dict_ksm.opd[op]).replace("0x", "").zfill(2)
            if self.lablere.match(op):
                # Lable
                print("Lable", i, ":", op[0 : -1])
                i += 1
                continue
            arg1, arg2 = 0,0
            try:
                arg1 = k[1]
                arg2 = k[2]
            except IndexError:
                # Only has one arg
                arg1 = k[1]
            print("OP code", i, ":", op, arg1, arg2 if arg2 else "")
            i += 1
            arg1, arg1mem = hexfix(arg1)
            if arg2:
                arg2, arg2mem = hexfix(arg2)
            # Get the proper mode
            mode = getmode(arg1mem, arg2mem if arg2mem else 0)
            final = assemble_op(op, arg1, arg2 if arg2 else None, mode)
