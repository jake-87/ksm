#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
void printer(int64_t a) {
    printf("%c0x%lx\n", a < 0 ? '-' : ' ', (uint64_t) labs(a));
}
int64_t scanner() {
    uint64_t temp;
    scanf("%lx", &temp);
    int64_t ret = (int64_t) temp;
    return ret;
}
void flusher() {
    fflush(stdout);
    fflush(stderr);
}