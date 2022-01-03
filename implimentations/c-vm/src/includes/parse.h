#pragma once
#include "libs.h"
typedef struct _file_string_t {
    char * ins;
    int64_t size;
} file_string_t;
int parse(FILE * fp, int debug, int64_t memsize);