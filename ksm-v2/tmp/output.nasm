
bits 64
section .data
    pointer dq 1
    argv dq 1
    argc dq 1
    _they_are_equal____KSM_INTERNAL_: db "they are equal", 0xa, "", 0
    _all_done____KSM_INTERNAL_: db "all done", 0xa, "", 0

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

   mov qword rax, 1
   mov qword r9, rax
; mov r9 1


   mov qword rax, 1
   mov qword r10, rax
; mov r10 1


   mov qword rax, r10
   mov qword rbx, r9
   cmp rax, rbx
; cmp r9 r10


je equal
; je equal 


equal:
; equal:  

   push r9
   push r10
   push r11
   mov qword rdi, _they_are_equal____KSM_INTERNAL_
   call print_string
   pop r11
   pop r10
   pop r9

; print_string they are equal\n

   mov qword rcx, [pointer]
jmp done
; jmp done 


done:
; done:  

   push r9
   push r10
   push r11
   mov qword rdi, _all_done____KSM_INTERNAL_
   call print_string
   pop r11
   pop r10
   pop r9

; print_string all done\n

   mov qword rcx, [pointer]
   push r9
   push r10
   push r11
   mov qword rdi, 10
   call print_int
   pop r11
   pop r10
   pop r9
; print_int 10 


   mov qword rcx, [pointer]
   push r9
   push r10
   push r11
   mov qword rdi, 10
   call print_hex
   pop r11
   pop r10
   pop r9
; print_hex 10 


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
   mov qword rdi, 0
   mov qword rax, 60
   syscall
; hlt 0 


