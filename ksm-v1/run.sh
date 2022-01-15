#! /bin/bash
usage() {
    printf "USAGE: ./run.sh <module> <options>\n\n"
    printf "modules: python-vm c-vm fortran-vm nodejs-vm c-transpiler python-assembler help\n\n"
    printf "*-vm: ./run.sh <module> <path to ksm file> <memory amount> [debug: bool]\n"
    printf "*-transpiler: ./run.sh <module> <path to ksm file> <memory amount>\n"
    printf "*-assembler: ./run.sh <module> <path to ksm-asm file> [debug: bool]\n"
    printf "help: ./run.sh help\n"
}
if [ $# -lt 2 ]; then
    if [ "$1" == "help" ]; then
        printf "\n Requirements for all impls: POSIX sh, Bash\n"
        printf "c-*: GCC\n"
        printf "fortran-*: Gfortran\n"
        printf "python-*: python3\n"
        printf "nodejs-*: node >= 12\n"
        printf "htmljs-*: modern browser\n"
        exit
    fi
    usage
    exit
fi
# VMs
path="../../${2}"
if [ "$1" == "python-vm" ]; then
    cd implementations/python-vm
    ./output $path $3 $4
elif [ "$1" == "c-vm" ]; then
    cd implementations/c-vm
    ./build.sh
    ./output $path $3 $4
elif [ "$1" == "fortran-vm" ]; then
    cd implementations/fortran-vm
    printf "\n Warning: Fortran VM does not support debug\n\n"
    ./build.sh
    ./output $path $3
elif [ "$1" == "nodejs-vm" ]; then
    cd implementations/nodejs-vm
    ./output $path $3 $4
elif [ "$1" == "c-transpiler" ]; then
    printf "output avalible as implimentations/c-transpiler/ksm-output\n\n"
    cd implementations/c-transpiler
    ./output $path $3
elif [ "$1" == "c-nasm-transpiler" ]; then
    printf "output avalible as implimentations/c-nasm-transpiler/ksm-output\n\n"
    cd implementations/c-nasm-transpiler
    ./output $path $3 | tee mylog.log
elif [ "$1" == "python-assembler" ]; then
    cd implementations/python-assembler-v2
    ./output $path $3
else
    usage
    exit
fi
exit