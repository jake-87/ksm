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
main:
    mov rax, 
    mov rbx, 8
    imul rax, rbx
    mov rdi, rax
    call malloc
    mov [pointer], rax

; end prelude
