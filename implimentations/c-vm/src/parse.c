#include "includes/libs.h"
#include "includes/ops.h"
#include "includes/parse.h"
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
int parse(FILE * fp, int debug, int64_t memsize) {
    if (fp == NULL) {
        fprintf(stderr, "Couldn't open file\n");
        exit(1);
    }
    file_string_t fs = read_file(fp);
    printf("%s\n %ld\n", fs.ins, fs.size);
    return 0;
}