import CPU
import conf
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
            pc = cpu.mem[0]
            if not arr[cpu.mem[0]]:
                raise OSError("Program terminatied unexpectedly.")
            pr = cpu.call(op=arr[cpu.mem[0]][0], arg1=arr[cpu.mem[0]][1], arg2=arr[cpu.mem[0]][2], arg3=arr[cpu.mem[0]][3])
            if debug:
                print(arr[pc][0], arr[pc][1], arr[pc][2], arr[pc][3], end = ":" + str(" " * (conf.ljust - 4)))
                k = [hex(n) for n in cpu.mem]
                for n in k:
                    print(n.ljust(conf.ljust), end=" ")
                print(" | ", hex(cpu.cmp))
            if pr:
                ifexit = "dontexit"
                try:
                    ifexit = pr[0]
                except:
                    pr()
                if ifexit != "dontexit":
                    exit(pr[1])
            cpu.mem[0] += 1
