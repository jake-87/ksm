#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
void flusher() {
    fflush(stdout);
    fflush(stderr);
}
void print_hex(int64_t a) {
    printf("%c0x%lx\n", a < 0 ? '-' : ' ', (uint64_t) labs(a));
    flusher();
}
void print_int(int64_t a) {
    printf("%ld\n", a);
    flusher();
}
void print_string(char * a) {
    puts(a);
}