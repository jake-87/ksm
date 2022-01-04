#/bin/bash

if [ "$#" -ne 3 ]; then
    if [ "$#" -ne 1 ]; then
        echo "Illegal number of parameters"
        echo "Useage: ./transpile.sh <ksm file> <output file> <memory>"
        exit
    else
        k="native-output"
        j="1024"
    fi
else
    k=$2
    j=$3
fi
# -O3 is faster, i've found, and there's not much to break
CARGS="-O3 -Wall -Wextra -pedantic -Wno-unused-parameter"
CARGS="$CARGS -Wno-unused-parameter -Wno-stringop-truncation -Wno-string-concatenation "
CARGS="$CARGS -Wno-unknown-warning-option -Wno-newline-eof"
CC=cc
$CC src/*.c -o output $CARGS
cat transpile/preamble.c > $k.c
printf "int main () {\n" >> $k.c
printf "cpu_t cpu;\n" >> $k.c
printf "cpu.mem = malloc(sizeof(int64_t) * $j);\n" >> $k.c
printf "/* END PREAMBLE */\n\n" >> $k.c
./output $1 >> $k.c
printf "\n/* POSTAMBLE */\n" >> $k.c
printf "free(cpu.mem);\n}" >> $k.c
printf "\n/* END POSTAMBLE */\n" >> $k.c
$CC $k.c -o $k $CARGS
rm output