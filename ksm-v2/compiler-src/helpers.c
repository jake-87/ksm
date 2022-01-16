#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
void flusher() {
    fflush(stdout);
    fflush(stderr);
}
void print_hex(int64_t a) {
    printf("%c0x%lx", a < 0 ? '-' : ' ', (uint64_t) labs(a));
    /*
        Broken down:

        %c : a < 0 ? '-' : ' '
        This prints either a minus sign if a is negative, or a space if it is not.

        0x : prints "0x"

        %lx : (uint64_t) labs(a)
        This prints the positive representation of "a", cast to a uint64_t.

        \n : prints '\n
    */
    flusher();
}
void print_int(int64_t a) {
    printf("%ld", a);
    flusher();
}
void print_string(char * a) {
    printf("%s", a);
    flusher();
}

void print_newline() {
    puts("");
}