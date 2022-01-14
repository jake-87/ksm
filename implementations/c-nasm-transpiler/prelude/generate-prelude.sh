cat << EOF
bits 64
section .data
    pointer dq 1
    temp dq 1
section .text
    global main
    extern printer
    extern scanner
    extern my_exit
    extern malloc
    extern flusher
main:
    mov rax, $1
    mov rbx, 8
    imul rax, rbx
    mov rdi, rax
    call malloc
    mov qword [pointer], rax
    mov qword rcx, [pointer]
; end prelude
EOF