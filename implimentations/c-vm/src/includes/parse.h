#pragma once
#include "libs.h"
// simple struct to store instructions and size
typedef struct _file_string_t {
    char * ins;
    int64_t size;
} file_string_t;
void slice_str(const char * str, char * output, size_t start, size_t end);
file_string_t read_file(FILE * fp);
int parse(FILE * fp, int debug, int64_t memsize);