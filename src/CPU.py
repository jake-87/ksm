class cpu:
    def __init__(self, memsize):
        self.mem = [0 for i in range(memsize)]
        self.cmp = 0
        self.special = ["08", "09", "0a", "0d", "0e", "0f"]
        self.op = {
            "00": self.__op00,
            "01": self.__op01,
            "02": self.__op02,
            "03": self.__op03,
            "04": self.__op04,
            "05": self.__op05,
            "06": self.__op06,
            "07": self.__op07,
            "08": self.__op08,
            "09": self.__op09,
            "0a": self.__op0a,
            "0b": self.__op0b,
            "0c": self.__op0c,
            "0d": self.__op0d,
            "0e": self.__op0e,
            "0f": self.__op0f,
            "10": self.__op10,
            "11": self.__op11,
            "12": self.__op12,
            "13": self.__op13,
            "14": self.__op14
        }
    def __shx(self, x):
        k = hex(int(x, 16))
        return k.replace("x", "")
    def __op00(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[arg1] = self.mem[arg2]
        else:
            self.mem[arg1] = arg2
    def __op01(self, arg1, arg2, arg3):
        self.mem[arg1] += 1
    def __op02(self, arg1, arg2, arg3):
        self.mem[arg1] -= 1
    def __op03(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] + self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] + arg2
        else:
            self.mem[1] = arg1 + arg2
    def __op04(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] - self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] - arg2
        else:
            self.mem[1] = arg1 - arg2
    def __op05(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] * self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] * arg2
        else:
            self.mem[1] = arg1 * arg2
    def __op06(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] // self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] // arg2
        else:
            self.mem[1] = arg1 // arg2
    def __op07(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.cmp = self.mem[arg1] - self.mem[arg2]
        elif arg3 == 2:
            self.cmp = self.mem[arg1] - arg2
        else:
            self.cmp = arg1 - arg2
    def __op08(self, arg1, arg2, arg3):
        self.mem[0] = int(arg1 + arg2 + arg3, 16) // 4
    def __op09(self, arg1, arg2, arg3):
        if self.cmp == 0:
            self.mem[0] = int(arg1 + arg2 + arg3, 16) // 4
    def __op0a(self, arg1, arg2, arg3):
        if self.cmp != 0:
            self.mem[0] = int(arg1 + arg2 + arg3, 16) // 4
    def __op0b(self, arg1, arg2, arg3):
        if arg2 == 1:
            print("\n\n\n" + hex(self.mem[arg1]) + "\n\n\n")
        else:
            print(hex(arg1))
    def __op0c(self, arg1, arg2, arg3):
        self.mem[arg1] = input(">")
    def __op0d(self, arg1, arg2, arg3):
        if arg2 == 1:
            print("0d", arg1, arg2, str(arg3) + ": HALT")
            exit(self.mem[arg1])
        else:
            print("0d", arg1, arg2, str(arg3) + ": HALT")
            exit(arg1)
    def __op0e(self, arg1, arg2, arg3):
        self.mem[int(arg1 + arg2 + arg3, 16)] = self.mem[1]
    def __op0f(self, arg1, arg2, arg3):
        self.mem[1] = self.mem[int(arg1 + arg2 + arg3, 16)]
    def __op10(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] ^ self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] ^ arg2
        else:
            self.mem[1] = arg1 ^ arg2
    def __op11(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] & self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] & arg2
        else:
            self.mem[1] = arg1 & arg2
    def __op12(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] | self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] | arg2
        else:
            self.mem[1] = arg1 | arg2
    def __op13(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = ~ self.mem[arg1]
        else:
            self.mem[1] = ~ arg1
    def __op14(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] << self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] << arg2
        else:
            self.mem[1] = arg1 << arg2
    def __op14(self, arg1, arg2, arg3):
        if arg3 == 1:
            self.mem[1] = self.mem[arg1] >> self.mem[arg2]
        elif arg3 == 2:
            self.mem[1] = self.mem[arg1] >> arg2
        else:
            self.mem[1] = arg1 >> arg2
    def call(self, op, arg1, arg2, arg3):
        if op not in self.special:
            self.op[op](int(arg1), int(arg2), int(arg3))
        else:
            self.op[op](self.__shx(arg1), self.__shx(arg2), self.__shx(arg3))
