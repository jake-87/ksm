#/bin/sh
CARGS="-O2 -Wall -Wextra -pedantic -Wno-unused-parameter"
CARGS="$CARGS -Wno-unused-parameter -Wno-stringop-truncation -Wno-string-concatenation "
CARGS="$CARGS -Wno-unknown-warning-option -Wno-newline-eof"
CC=clang
$CC src/*.c -o output $CARGS