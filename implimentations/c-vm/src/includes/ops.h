#pragma once
#include "libs.h"
// defines to make the process of writing functions eaiser
#define IVO(x) void op##x
// seperate ARGS and CPU for clarity
#define ARGS int64_t a1, int64_t a2, int64_t a3
// CPU struct
typedef struct _cpu_t {
    int64_t * mem;
    int64_t cmp;
} cpu_t;
#define CPU cpu_t * cpu
// makes stuff quicker
#define a3_1 if ((a3) == 1)
#define a3_2 if ((a3) == 2)
// special opcodes
// macros ftw 
IVO(00) (CPU, ARGS);
IVO(01) (CPU, ARGS);
IVO(02) (CPU, ARGS);
IVO(03) (CPU, ARGS);
IVO(04) (CPU, ARGS);
IVO(05) (CPU, ARGS);
IVO(06) (CPU, ARGS);
IVO(07) (CPU, ARGS);
IVO(08) (CPU, int64_t concat);
IVO(09) (CPU, int64_t concat);
IVO(0a) (CPU, int64_t concat);
IVO(0b) (CPU, ARGS);
IVO(0c) (CPU, ARGS);
IVO(0d) (CPU, ARGS);
IVO(0e) (CPU, int64_t concat);
IVO(0f) (CPU, int64_t concat);
IVO(10) (CPU, ARGS);
IVO(11) (CPU, ARGS);
IVO(12) (CPU, ARGS);
IVO(13) (CPU, ARGS);
IVO(14) (CPU, ARGS);
IVO(15) (CPU, ARGS);
IVO(16) (CPU, int64_t concat);
IVO(17) (CPU, ARGS);
IVO(18) (CPU, ARGS);