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
    mov rax, 10
    mov rbx, 8
    imul rax, rbx
    mov rdi, rax
    call malloc
    mov qword [pointer], rax
    mov qword rcx, [pointer]
; end prelude
    mov qword [rcx + 1 * 8], 5
;00 01 05 02

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 3 * 8], rax
;00 03 01 01

    mov qword [rcx + 2 * 8], 1
;00 02 01 02

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, [rcx + 2 * 8]
    imul rax, rbx
    mov qword [rcx + 1 * 8], rax
;05 03 02 01

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 2 * 8], rax
;00 02 01 01

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, 1
    sub rax, rbx
    mov qword [rcx + 1 * 8], rax
;04 03 01 02

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 3 * 8], rax
;00 03 01 01

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, [rcx + 2 * 8]
    imul rax, rbx
    mov qword [rcx + 1 * 8], rax
;05 03 02 01

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 2 * 8], rax
;00 02 01 01

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, 1
    sub rax, rbx
    mov qword [rcx + 1 * 8], rax
;04 03 01 02

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 3 * 8], rax
;00 03 01 01

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, [rcx + 2 * 8]
    imul rax, rbx
    mov qword [rcx + 1 * 8], rax
;05 03 02 01

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 2 * 8], rax
;00 02 01 01

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, 1
    sub rax, rbx
    mov qword [rcx + 1 * 8], rax
;04 03 01 02

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 3 * 8], rax
;00 03 01 01

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, [rcx + 2 * 8]
    imul rax, rbx
    mov qword [rcx + 1 * 8], rax
;05 03 02 01

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 2 * 8], rax
;00 02 01 01

    mov qword rax, [rcx + 3 * 8]
    mov qword rbx, 1
    sub rax, rbx
    mov qword [rcx + 1 * 8], rax
;04 03 01 02

    mov qword rax, [rcx + 1 * 8]
    mov qword [rcx + 3 * 8], rax
;00 03 01 01

    mov qword rdi, [rcx + 2 * 8]
    call printer
;0b 02 01 00

    mov qword rax, 60
    mov qword rdi, 0
    syscall
