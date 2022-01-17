import sys
import generate_asm
# helper
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
def main():
    with open(sys.argv[1]) as fp:
        data = fp.read()
    data = data.replace(",", "")
    data = data.split("\n")
    status = generate_asm.status_t(0, 0)
    nasm_code = ""
    data_section = ""
    pre = generate_asm.prelude(int(sys.argv[2]))
    data_section += pre[0]
    nasm_code += pre[1]
    for asm in data:
        asm = asm.strip()
        tmp = generate_asm.gen(status, asm)
        if tmp[0] == 0:
            nasm_code += tmp[1]
        else:
            data_section += tmp[1][0]
            nasm_code += tmp[1][1]
            nasm_code += tmp[2]
    print(data_section + "\n;end data section\n\n" + nasm_code)
    exit(0)
if __name__ == "__main__":
    main()