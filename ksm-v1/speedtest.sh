#! /usr/bin/env bash
impls=(python-vm c-vm nodejs-vm fortran-vm c-transpiler c-nasm-transpiler)
for k in "${impls[@]}"; do
    cd implementations/$k
    echo $k
    ./speedtest.sh
    cd ../..
    printf "\n\n\n"
done
