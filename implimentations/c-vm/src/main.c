#include "includes/libs.h"
#include "includes/parse.h"
#define MIN_MEMSIZE 1024

int main(int argc, char ** argv) {
    int debug = 0;
    int64_t memsize = 0;
    if (argc < 2) {
        fprintf(stderr, "No file given\n");
    }
    FILE * fp;
    fp = fopen(argv[1], "r");
    if (argc > 2) {
        sscanf(argv[2], "%ld", &memsize);
    }
    if (argc > 3) {
        sscanf(argv[3], "%d", &debug);
    }
    if (!memsize) {
        memsize = MIN_MEMSIZE;
    }
    parse(fp, debug, memsize);
    printf("done %d %p %ld\n",debug, (void *)fp, memsize);
    return 0;
}