#include "includes/libs.h"
#include "includes/ops.h"
// instructions for vm, see header for macros
IVO(00) (CPU, ARGS) {
    a3_1 {
        cpu->mem[a1] = cpu->mem[a2];
        printf("cpu.mem[%ld] = cpu.mem[%ld];\n", a1, a2);
    }
    a3_2 {
        cpu->mem[a1] = a2;
        printf("cpu.mem[%ld] = %ld;\n", a1, a2);
    }
}
IVO(01) (CPU, ARGS) {
    cpu->mem[a1]++;
    printf("cpu.mem[%ld]++;\n", a1);
}
IVO(02) (CPU, ARGS) {
    cpu->mem[a1]--;
    printf("cpu.mem[%ld]++;\n", a1);
}
IVO(03) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] + cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] + cpu.mem[%ld];\n", a1, a2);
    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] + a2;
        printf("cpu.mem[1] = cpu.mem[%ld] + %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 + a2;
        printf("cpu.mem[1] = %ld + %ld;\n", a1, a2);
    }
}
IVO(04) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] - cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] - cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] - a2;
        printf("cpu.mem[1] = cpu.mem[%ld] - %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 - a2;
        printf("cpu.mem[1] = %ld - %ld;\n", a1, a2);

    }
}
IVO(05) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] * cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] * cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] * a2;
        printf("cpu.mem[1] = cpu.mem[%ld] * %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 * a2;
        printf("cpu.mem[1] = %ld * %ld;\n", a1, a2);
    }
}
IVO(06) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] / cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] / cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] / a2;
        printf("cpu.mem[1] = cpu.mem[%ld] / %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 / a2;
        printf("cpu.mem[1] = %ld / %ld;\n", a1, a2);
    }
}
IVO(07) (CPU, ARGS) {
    a3_1 {
        cpu->cmp = cpu->mem[a1] - cpu->mem[a2];
    }
    a3_2 {
        cpu->cmp = cpu->mem[a1] - a2;
    }
    else {
        cpu->cmp = a1 - a2;
    }
}
IVO(08) (CPU, int64_t concat) {
    cpu->mem[00] = concat / 4;
}
IVO(09) (CPU, int64_t concat) {
    if (!cpu->cmp) {
        cpu->mem[00] = concat / 4;
    }
}
IVO(0a) (CPU, int64_t concat) {
    if (cpu->cmp) {
        cpu->mem[00] = concat / 4;
    }
}
IVO(0b) (CPU, ARGS) {
    if (a2 == 01) {
        //printf("%c0x%lx\n", cpu->mem[a1] < 0 ? '-' : ' ', (uint64_t) labs(cpu->mem[a1]));
        printf("printf(\"");
        printf("%%");
        printf("c0x");
        printf("%%");
        printf("lx\\n\"");
        printf(", cpu.mem[%ld] < 0 ? '-' : ' ', (uint64_t) labs(cpu.mem[%ld]));\n", a1, a1);
    }
    else {
        //printf("%c0x%lx\n",a1 < 0 ? '-' : ' ', (uint64_t) labs(a1));
        printf("printf(\"");
        printf("%%");
        printf("c0x");
        printf("%%");
        printf("lx\\n\"");
        printf(", %ld < 0 ? '-' : ' ', (uint64_t) labs(%ld));\n", a1, a1);
    }
}
IVO(0c) (CPU, ARGS) {
    //uint64_t temp;
    //scanf("> %lx", &temp);
    //cpu->mem[a1] = (int64_t) temp;
    printf("uint64_t temp; scanf(\"> %%lx\", &temp); cpu.mem[%ld] = (int64_t) temp;\n", a1);
}
IVO(0d) (CPU, ARGS) {
    if (a2 == 01) {
        printf("exit(cpu.mem[%ld]);\n", a1);
        exit(cpu->mem[a1]);
    }
    else {
        printf("exit(%ld);\n", a1);
        exit(a1);
    }
}
IVO(0e) (CPU, int64_t concat) {
    cpu->mem[concat] = cpu->mem[01];
    printf("cpu.mem[%ld] = cpu.mem[1];\n", concat);
}
IVO(0f) (CPU, int64_t concat) {
    cpu->mem[01] = cpu->mem[concat];
    printf("cpu.mem[1] = cpu.mem[%ld];\n", concat);
}
IVO(10) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] ^ cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] ^ cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] ^ a2;
        printf("cpu.mem[1] = cpu.mem[%ld] ^ %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 ^ a2;
        printf("cpu.mem[1] = %ld ^ %ld;\n", a1, a2);
    }
}
IVO(11) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] & cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] & cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] & a2;
        printf("cpu.mem[1] = cpu.mem[%ld] & %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 & a2;
        printf("cpu.mem[1] = %ld & %ld;\n", a1, a2);
    }
}
IVO(12) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] | cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] | cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] | a2;
        printf("cpu.mem[1] = cpu.mem[%ld] | %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 | a2;
        printf("cpu.mem[1] = %ld | %ld;\n", a1, a2);
    }
}
IVO(13) (CPU, ARGS) {
    if (a2 == 1) {
        cpu->mem[01] = ~ cpu->mem[a1];
        printf("cpu.mem[1] = ~ cpu.mem[%ld];\n", a1);
    }
    else {
        cpu->mem[01] = ~ a1;
        printf("cpu.mem[1] = ~ %ld;\n", a1);
    }
}
IVO(14) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] << cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] << cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] << a2;
        printf("cpu.mem[1] = cpu.mem[%ld] << %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 << a2;
        printf("cpu.mem[1] = %ld << %ld;\n", a1, a2);
    }
}
IVO(15) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] >> cpu->mem[a2];
        printf("cpu.mem[1] = cpu.mem[%ld] >> cpu.mem[%ld];\n", a1, a2);

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] >> a2;
        printf("cpu.mem[1] = cpu.mem[%ld] >> %ld;\n", a1, a2);
    }
    else {
        cpu->mem[01] = a1 >> a2;
        printf("cpu.mem[1] = %ld >> %ld;\n", a1, a2);
    }
}
IVO(16) (CPU, int64_t concat) {
    cpu->mem[01] = concat;
    printf("cpu.mem[1] = %ld;\n", concat);
}
IVO(17) (CPU, ARGS) {
    cpu->mem[a1] = cpu->mem[cpu->mem[a2]];
    printf("cpu.mem[%ld] = cpu.mem[cpu.mem[%ld]];\n", a1, a2);
}
IVO(18) (CPU, ARGS) {
    a3_1 {
        cpu->mem[cpu->mem[a1]] = cpu->mem[a2];
        printf("cpu.mem[cpu.mem[%ld]] = cpu.mem[%ld];\n", a1, a2);
    }
    else {
        cpu->mem[cpu->mem[a1]] = a2;
        printf("cpu.mem[cpu.mem[%ld]] = %ld;\n", a1, a2);
    }
}