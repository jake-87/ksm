import ast
import re
import dict_ksm # This contains the info needed for ksm

lable_iter_dict = {}
lable_iter = 0
def hexfix(mhex):
    # Fix literals like "m0x91" into proper hex numbers, with an additional
    # bit for if it's a memory location
    if ":" in str(mhex):
        return (mhex, 0)
    if mhex[0].lower() == "m":
        ismem = "1"
    else:
        ismem = "0"
    mhex = mhex.replace("m", "")
    if "x" in mhex:
        return (hex(int(mhex, 16)).replace("0x", ""), ismem)
    return (hex(int(mhex)).replace("0x", ""), ismem)

def getmode_single(arg):
    if int(arg):
        return 1
    else:
        return 3

def getmode(arg1, arg2):
    # Return a mode, based on the mode table
    if arg1 and int(arg2):
        return 1
    if arg1 and not int(arg2):
        return 2
    if not arg1 and not int(arg2):
        return 3
    raise SyntaxError("Invalid mode")

def assemble_op(op, arg1, arg2, mode):
    # Assemble an opcode.
    global lable_iter_dict
    global lable_iter
    k = dict_ksm.k
    final_op = hex(dict_ksm.opd[op]).replace("0x", "")
    if op in k[0]: # Using a lable
        if arg1 in lable_iter_dict:
            pass
        else:
            lable_iter_dict[arg1] = hex(lable_iter).replace("0x", "").zfill(6)
            lable_iter += 1
        return final_op.zfill(2) + lable_iter_dict[arg1]
    if op in k[1]:
        return final_op.zfill(2) + arg1.zfill(2) + "".zfill(4)
    if op in k[2]:
        return final_op.zfill(2) + arg1.zfill(6)
    if op in k[3]:
        return final_op.zfill(2) + arg1.zfill(2) + mode.zfill(2) + "00"
    if op in k[4]:
        return final_op.zfill(2) + arg1.zfill(2) + arg2.zfill(2) + "00"
    else:
        return final_op.zfill(2) + arg1.zfill(2) + arg2.zfill(2) + mode.zfill(2)

class codegenerator():
    def __init__(self, tok_mast):
        self.ast = tok_mast
        self.lablere = re.compile("^[^\:]+:")
    def gencode_ksm(self, debug = False):
        global lable_iter_dict
        global lable_iter
        mast = self.ast.get_tok()
        i = 1 # Counter for debug
        semi_final_opcodes = []
        for k in mast:
            # For each token
            op = k[0]
            if self.lablere.match(op):
                # Lable
                if debug:
                    print(i, ": Lable", ":", "\"" + str(op) + "\"")
                i += 1
                semi_final_opcodes.append(op)
                continue
            # Not lable
            arg1, arg2 = 0, None
            try:
                arg1 = k[1]
                arg2 = k[2]
            except IndexError:
                # Only has one arg
                arg1 = k[1]
            if debug:
                print(i, ": OP code", ":", op, arg1, arg2 if arg2 else "")
            if op not in dict_ksm.k[0]:
                arg1, arg1mem = hexfix(arg1)
                if arg2 != None:
                    arg2, arg2mem = hexfix(arg2)
            # Get the proper mode
            mode = 0
            if op in dict_ksm.k[3]:
                mode = getmode_single(str(arg1mem))
            else:
                mode = getmode(arg1mem, arg2mem if arg2mem else 0)
            # Assemble the opcode
            final_op = assemble_op(op, str(arg1), str(arg2) if arg2 else None, str(mode))
            semi_final_opcodes.append(final_op)
            if debug:
                print(i, ": Assembled OP code", ":", final_op) 
            i += 1
        
        count = 0
        final_lables = {}
        for each in semi_final_opcodes:
            if not self.lablere.match(each):
                count += 4
            else:
                final_lables[lable_iter_dict[each[0:-1]]] = count - 4
            print(each, count)
        if debug:
           print("Semi-final OP codes: ", semi_final_opcodes)
           print("Lables: ", final_lables)
        final_ops = []
        for each in semi_final_opcodes:
            if self.lablere.match(each):
                continue
            if each[0:2] in dict_ksm.jmps:
                op = each[0:2]
                jump = final_lables[each[2:len(each)]]
                final_ops.append(op + hex(int(jump)).replace("0x", "").zfill(6))
            else:
                final_ops.append(each)
        if debug:
            print("Final ops:", final_ops)
        return "".join(final_ops)
