#include "includes/libs.h"
#include "includes/ops.h"
// instructions for vm, see header for macros
IVO(00) (CPU, ARGS) {
    a3_1 {
        cpu->mem[a1] = cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a2);
        printf("    mov qword [rcx + %ld * 8], rax\n", a1);
    }
    a3_2 {
        cpu->mem[a1] = a2;
        if_rcx_mod
        printf("    mov qword [rcx + %ld * 8], %ld\n", a1, a2);
    }
}
IVO(01) (CPU, ARGS) {
    cpu->mem[a1]++;
    if_rcx_mod
    printf("    inc qword [rcx + %ld * 8]\n", a1);
}
IVO(02) (CPU, ARGS) {
    cpu->mem[a1]--;
    if_rcx_mod
    printf("    dec qword [rcx + %ld * 8]\n", a1);
}
IVO(03) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] + cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    add rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] + a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    add rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 + a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    add rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(04) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] - cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    sub rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] - a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    sub rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 - a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    sub rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(05) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] * cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    imul rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] * a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    imul rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 * a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    imul rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(06) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] / cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    idiv rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] / a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    idiv rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 / a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    idiv rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
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
        if_rcx_mod
        printf("    mov qword rdi, [rcx + %ld * 8]\n", a1);
        printf("    call printer\n");
        cpu->rcx = 1;
        //printf("%c0x%lx\n", cpu->mem[a1] < 0 ? '-' : ' ', (uint64_t) labs(cpu->mem[a1]));
        
    }
    else {
        printf("    mov qword temp, %ld", a1);
        printf("    mov qword rdi, [temp]\n");
        printf("    call printer\n");
        //printf("%c0x%lx\n",a1 < 0 ? '-' : ' ', (uint64_t) labs(a1));
        
    }
}
IVO(0c) (CPU, ARGS) {
    //uint64_t temp;
    //scanf("%lx", &temp);
    //cpu->mem[a1] = (int64_t) temp;
    if_rcx_mod
    printf("    call scanner\n");
    printf("    mov qword [rcx + %ld * 8], rax", a1);
    cpu->rcx = 1;
}
IVO(0d) (CPU, ARGS) {
    if (a2 == 01) {
        if_rcx_mod
        printf("    call flusher\n");
        printf("    mov qword rax, 60\n");
        printf("    mov qword rdi, [rcx + %ld * 8]\n", a1);
        printf("    syscall\n");
        exit(cpu->mem[a1]);
    }
    else {
        printf("    call flusher\n");
        printf("    mov qword rax, 60\n");
        printf("    mov qword rdi, %ld\n", a1);
        printf("    syscall\n");
        exit(a1);
    }
}
IVO(0e) (CPU, int64_t concat) {
    cpu->mem[concat] = cpu->mem[01];
    if_rcx_mod
    printf("    mov qword rax, [rcx + %ld * 8]\n", concat);
    printf("    mov qword [rcx + 1 * 8], rax\n");
}
IVO(0f) (CPU, int64_t concat) {
    cpu->mem[01] = cpu->mem[concat];
    if_rcx_mod
    printf("    cpu.mem[1] = cpu.mem[%ld];\n", concat);
    printf("    mov qword rax, [rcx + 1 * 8]q\n");
    printf("    mov qword [rcx + %ld * 8], rax\n", concat);
}
IVO(10) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] ^ cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    xor rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] ^ a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    xor rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 ^ a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    xor rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(11) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] & cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    and rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] & a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    and rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 & a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    and rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(12) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] | cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    or rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] | a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    or rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 | a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    or rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(13) (CPU, ARGS) {
    if (a2 == 1) {
        cpu->mem[01] = ~ cpu->mem[a1];
        if_rcx_mod
        printf("    mov rax, [rcx + %ld * 8]\n", a1);
        printf("    not rax\n");
        printf("    mov [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = ~ a1;
        if_rcx_mod
        printf("    mov rax, %ld\n", a1);
        printf("    not rax\n");
        printf("    mov [rcx + 1 * 8], rax\n");
    }
}
IVO(14) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] << cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    shl rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] << a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    shl rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 << a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    shl rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(15) (CPU, ARGS) {
    a3_1 {
        cpu->mem[01] = cpu->mem[a1] >> cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    shr rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");

    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] >> a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    shr rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
    else {
        cpu->mem[01] = a1 >> a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    shr rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rax\n");
    }
}
IVO(16) (CPU, int64_t concat) {
    cpu->mem[01] = concat;
    if_rcx_mod
    printf("    mov qword [rcx + 1 * 8], %ld", concat);
}
IVO(17) (CPU, ARGS) {
    cpu->mem[a1] = cpu->mem[cpu->mem[a2]];
    printf("cpu.mem[%ld] = cpu.mem[cpu.mem[%ld]];\n", a1, a2);
    if_rcx_mod
    printf("    mov qword rbx, [rcx + %ld * 8]\n", a1);
    printf("    mov qword rax, [rcx + rbx * 8]\n");
    printf("    mov qword [rcx + %ld * 8], rax", a2);
}
IVO(18) (CPU, ARGS) {
    a3_1 {
        cpu->mem[cpu->mem[a1]] = cpu->mem[a2];
        if_rcx_mod
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rax, [rcx + %ld * 8]\n", a2);
        printf("    mov qword [rcx + rbx * 8], rax");
    }
    else {
        cpu->mem[cpu->mem[a1]] = a2;
         if_rcx_mod
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rax, %ld\n", a2);
        printf("    mov qword [rcx + rbx * 8], rax");
    }
}
IVO(19) (CPU, int64_t concat) {
    if (cpu->cmp > 0) {
        cpu->mem[00] = concat / 4;
    }
}
IVO(1a) (CPU, int64_t concat) {
    if (cpu->cmp < 0) {
        cpu->mem[00] = concat / 4;
    }
}
IVO(1b) (CPU, ARGS) {
    if (a2 == 1) {
        cpu->st++;
        cpu->stack[cpu->st] = cpu->mem[a1];
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    push rax\n");
    }
    else {
        cpu->st++;
        cpu->stack[cpu->st] = a1;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    push rax\n");
    }
}
IVO(1c) (CPU, ARGS) {
    cpu->mem[a1] = cpu->stack[cpu->st];
    cpu->st--;
    printf("    pop rax\n");
    printf("    mov qword [rcx + %ld * 8], rax\n", a1);
}
IVO(1d) (CPU, ARGS) {
    if_rcx_mod
    a3_1 {
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, [rcx + %ld * 8]\n", a2);
        printf("    idiv rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rdx\n");
    }
    a3_2 {
        cpu->mem[01] = cpu->mem[a1] & a2;
        if_rcx_mod
        printf("    mov qword rax, [rcx + %ld * 8]\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    idiv rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rdx\n");
    }
    else {
        cpu->mem[01] = a1 & a2;
        if_rcx_mod
        printf("    mov qword rax, %ld\n", a1);
        printf("    mov qword rbx, %ld\n", a2);
        printf("    idiv rax, rbx\n");
        printf("    mov qword [rcx + 1 * 8], rdx\n");
}