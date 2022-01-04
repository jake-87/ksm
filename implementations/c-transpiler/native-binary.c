/* PREAMBLE */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef struct _cpu_t {
    int64_t * mem;
    int64_t cmp;
} cpu_t;

int main () {
cpu_t cpu;
cpu.mem = malloc(sizeof(int64_t) * 17);
/* END PREAMBLE */

/* 00 01 10 02 */ cpu.mem[1] = 16;
/* 01 02 00 00 */ cpu.mem[2]++;
/* 02 02 00 00 */ cpu.mem[2]++;
/* 03 05 04 03 */ cpu.mem[1] = 5 + 4;
/* 04 04 01 03 */ cpu.mem[1] = 4 - 1;
/* 05 02 04 03 */ cpu.mem[1] = 2 * 4;
/* 06 03 06 03 */ cpu.mem[1] = 3 / 6;
/* 0b 01 01 00 */ printf("%c0x%lx\n", cpu.mem[1] < 0 ? '-' : ' ', (uint64_t) labs(cpu.mem[1]));
/* 0c 03 00 00 */ uint64_t temp; scanf("> %lx", &temp); cpu.mem[3] = (int64_t) temp;
/* 0e 00 00 10 */ cpu.mem[16] = cpu.mem[1];
/* 0f 00 00 10 */ cpu.mem[1] = cpu.mem[16];
/* 0d 00 03 00 */ exit(768);

/* POSTAMBLE */
free(cpu.mem);
}
/* END POSTAMBLE */
