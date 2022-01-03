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
};
char * special_ins[] = {"08", "09", "0a", "0d", "0e", "0f", "15"};
int32_t special_ins_size = 7;
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
inline int64_t ins_index(int64_t x, int64_t y) {
    return x * 8 + y;
}
void slice_str(const char * str, char * output, size_t start, size_t end) {
    strncpy(output, str + start, end - start);
}
int parse(FILE * fp, int debug, int64_t memsize) {
    if (fp == NULL) {
        fprintf(stderr, "Couldn't open file\n");
        exit(1);
    }
    file_string_t fs = read_file(fp);
    printf("%s\n %ld\n", fs.ins, fs.size);
    cpu_t main_cpu;
    main_cpu.mem = malloc(sizeof(int64_t) * memsize);
    while (1) {

    }
    return 0;
}