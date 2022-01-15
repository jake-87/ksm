/* PREAMBLE */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef struct _cpu_t {
    int64_t * mem;
    int64_t cmp;
    int64_t st;
    int64_t stack[1024];
} cpu_t;

