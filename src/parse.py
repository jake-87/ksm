import CPU
def __ckstr(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
def parse(file, debug=0, memory = 16):
    with open(file, "r") as f:
        f = f.read().replace(" ", "").replace("    ", "").replace("\n", "").replace("\r", "")
        arr = [0 for i in range(len(f))]
        i = 0
        for chunk in __ckstr(f, 8):
            chunk = str(chunk)
            op   = chunk[0:2]
            arg1 = chunk[2:4]
            arg2 = chunk[4:6]
            arg3 = chunk[6:8]
            arr[i] = [op, arg1, arg2, arg3]
            i += 1
        cpu = CPU.cpu(memory)
        cpu.mem[0] = 0
        while 1:
            if not arr[cpu.mem[0]]:
                raise OSError("Program terminatied unexpectedly.")
            cpu.call(op=arr[cpu.mem[0]][0], arg1=arr[cpu.mem[0]][1], arg2=arr[cpu.mem[0]][2], arg3=arr[cpu.mem[0]][3])
            if debug:
                print(arr[cpu.mem[0]][0], arr[cpu.mem[0]][1], arr[cpu.mem[0]][2], arr[cpu.mem[0]][3], end=": ")
                k = [hex(n) for n in cpu.mem]
                for n in k:
                    print(n.ljust(6), end=" ")
                k = ", ".join(k)
                print("")
            cpu.mem[0] += 1
