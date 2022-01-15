#! /usr/bin/env bash
file=$1
output=$2
mem=$3
if [ "$2" == "printer" ]; then
    echo "output cannot be printer"
    exit
fi
CC=clang
CARGS="-O3 -Wall -Wextra -pedantic -Wno-unused-parameter"
CARGS="$CARGS -Wno-unused-parameter -Wno-stringop-truncation -Wno-string-concatenation "
CARGS="$CARGS -Wno-unknown-warning-option -Wno-newline-eof"
./prelude/generate-prelude.sh $mem > $output.nasm
$CC src/*.c -o tmp-output -g $CARGS
./tmp-output $file >> $output.nasm
rm tmp-output
nasm -f elf64 -o $output.o $output.nasm -F dwarf
$CC printer/printer.c -o printer.o -c -g $CARGS
$CC $output.o printer.o -o $output -static -g $CARGS
rm printer.o $output.o $output.nasm
