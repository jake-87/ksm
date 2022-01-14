#! /usr/bin/env bash
set -x
file=$1
output=$2
mem=$3
if [ "$2" == "printer" ]; then
    echo "output cannot be printer"
    exit
fi
./prelude/generate-prelude.sh $mem > $output.nasm
cc src/*.c -o tmp-output
./tmp-output $file >> $output.nasm
rm tmp-output
nasm -f elf64 -o $output.o $output.nasm -F dwarf
cc printer/printer.c -o printer.o -c -g 
cc $output.o printer.o -o $output -static -g 
rm printer.o $output.o