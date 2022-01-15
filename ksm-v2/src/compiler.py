import sys
import generate_asm
def main():
    with open(sys.argv[1]) as fp:
        data = fp.read()
    data = data.replace(",", "")
    data = data.split("\n")
    print(data)
    status = generate_asm.status(0, 0)
    nasm_code = ""
    data_section = ""
    nasm_code += generate_asm.prelude(int(sys.argv[2]))
    for asm in data:
        asm = asm.strip()
        tmp = generate_asm.gen(status, asm)
        nasm_code += tmp[1]
    print(nasm_code + data_section)
    exit(0)
if __name__ == "__main__":
    main()