#include "includes/libs.h"
#include "includes/ops.h"
#include "includes/parse.h"
// pointers to the ops functions
void (*op_table[])() = {
    op00,
    op01,
    op02,
    op03,
    op04,
    op05,
    op06,
    op07,
    op08,
    op09,
    op0a,
    op0b,
    op0c,
    op0d,
    op0e,
    op0f,
    op10,
    op11,
    op12,
    op13,
    op14,
    op15,
    op16,
    op17,
    op18,
    op19,
    op1a,
};
char * special_ins[] = {"08", "09", "0a", "0d", "0e", "0f", "15", "16", "19", "1a"};
char * jmps[] = {"07", "08", "09", "0a"};
int8_t jmp_size = 4;
int32_t special_ins_size = 10;
// test if string in array
inline int8_t in_strarr(char ** strarr, int32_t size, char * tst) {
    for (int i = 0; i < size; i++) {
        if (strcmp(strarr[i], tst) == 0) {
            return 1;
        }
    }
    return 0;
}

// read a file into a file_string_t
file_string_t read_file(FILE * fp) {
    char ch;
    file_string_t fs;
    fs.ins = malloc(sizeof(char) * 64);
    int64_t counter = 0;
    int64_t cur_size = 64;
    while ((ch = fgetc(fp)) != EOF) {
        if (counter > (cur_size - 1)) {
            cur_size += 64;
            fs.ins = realloc(fs.ins, cur_size);
        }
        fs.ins[counter] = ch;
        counter++;
    }
    fs.size = counter;
    return fs;
}

// inline functions to get instruction index
inline int64_t iidex(int64_t x, int64_t y) {
    return x * 8 + y;
}
// slice string
inline void slice_str(const char * str, char * output, size_t start, size_t end) {
    strncpy(output, str + start, end - start);
}
int parse(FILE * fp, int debug, int64_t memsize) {
    if (fp == NULL) {
        fprintf(stderr, "Couldn't open file\n");
        exit(1);
    }
    file_string_t fs = read_file(fp);
    cpu_t main_cpu;
    main_cpu.cmp = 0;
    main_cpu.mem = calloc(sizeof(int64_t) * memsize, 1);
    main_cpu.mem[0] = 0;
    char * op = malloc(sizeof(char) * 3);
    char * a1 = malloc(sizeof(char) * 3);
    char * a2 = malloc(sizeof(char) * 3);
    char * a3 = malloc(sizeof(char) * 3);
    char * concat = malloc(sizeof(char) * 9);
    while (1) {
        if (main_cpu.mem[0] * 8 >= fs.size) { 
            fprintf(stderr, "Program exited unexpectedly\n");
            exit(1);
        }    
        slice_str(fs.ins, op, iidex(main_cpu.mem[0], 0), iidex(main_cpu.mem[0], 2));
        slice_str(fs.ins, a1, iidex(main_cpu.mem[0], 2), iidex(main_cpu.mem[0], 4));
        slice_str(fs.ins, a2, iidex(main_cpu.mem[0], 4), iidex(main_cpu.mem[0], 6));
        slice_str(fs.ins, a3, iidex(main_cpu.mem[0], 6), iidex(main_cpu.mem[0], 8));
        snprintf(concat, 8, "%s%s%s", a1, a2, a3);
        uint64_t op_int;
        uint64_t a1_int;
        uint64_t a2_int;
        uint64_t a3_int;
        uint64_t concat_int;
        sscanf(op, "%lx", &op_int);
        sscanf(a1, "%lx", &a1_int);
        sscanf(a2, "%lx", &a2_int);
        sscanf(a3, "%lx", &a3_int);
        sscanf(concat, "%lx", &concat_int);
        if (!in_strarr(jmps, jmp_size, op))
            printf("/* %s %s %s %s */ ", op, a1, a2, a3);
        if (in_strarr(special_ins, special_ins_size, op)) {
            op_table[op_int](&main_cpu, concat_int);
        }
        else {
            op_table[op_int](&main_cpu, a1_int, a2_int, a3_int);
        }
        main_cpu.mem[0]++;
    }
    free(op);
    free(a1);
    free(a2);
    free(a3);
    free(main_cpu.mem);
    printf("\n");
    return 0;
}
