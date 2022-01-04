#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef struct _cpu_t {
    int64_t * mem;
    int64_t cmp;
} cpu_t;

int main () {
cpu_t cpu;
cpu.mem = malloc(sizeof(int64_t) * native-binary);cpu.mem[1] = 5;
cpu.mem[3] = cpu.mem[1];
cpu.mem[2] = 1;
cpu.mem[1] = cpu.mem[3] * cpu.mem[2];
cpu.mem[2] = cpu.mem[1];
cpu.mem[1] = cpu.mem[3] - 1;
cpu.mem[3] = cpu.mem[1];
cpu.mem[1] = cpu.mem[3] * cpu.mem[2];
cpu.mem[2] = cpu.mem[1];
cpu.mem[1] = cpu.mem[3] - 1;
cpu.mem[3] = cpu.mem[1];
cpu.mem[1] = cpu.mem[3] * cpu.mem[2];
cpu.mem[2] = cpu.mem[1];
cpu.mem[1] = cpu.mem[3] - 1;
cpu.mem[3] = cpu.mem[1];
cpu.mem[1] = cpu.mem[3] * cpu.mem[2];
cpu.mem[2] = cpu.mem[1];
cpu.mem[1] = cpu.mem[3] - 1;
cpu.mem[3] = cpu.mem[1];
printf("%c0x%lx\n", cpu.mem[2] < 0 ? '-' : ' ', (uint64_t) labs(cpu.mem[2]));
exit(0);
free(cpu.mem);
}