
bits 64
section .data
    pointer dq 1
    argv dq 1
    argc dq 1
    _one_two_thee__KSM_INTERNAL_: db "one two thee"

;end data section


section .text
    global main
    extern malloc
    extern print_int
    extern print_hex
    extern print_string
    extern print_newline
    extern open_file
    extern file_getchar
    extern file_feof
main:
    mov qword [argc], rdi
    mov qword [argv], rsi
    mov rax, 1
    mov rbx, 8
    imul rax, rbx
    mov rdi, rax
    call malloc
    mov qword [pointer], rax
    mov qword rcx, [pointer]
; end prelude
   push r9
   push r10
   push r11
   mov qword rdi, _one_two_thee__KSM_INTERNAL_
   call print_string
   pop r11
   pop r10
   pop r9

; print_string one two thee

   mov qword rcx, [pointer]
   push r9
   push r10
   push r11
   call print_newline
   pop r11
   pop r10
   pop r9
; print_newline  


   mov qword rcx, [pointer]
   mov qword rdi, 9
   mov qword rax, 60
   syscall
; hlt 9 


