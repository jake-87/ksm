# The revised KSM standard

This is the standard for KSM-V2.

This version of KSM is *not* interpreted, and is purely compiled. However, it still contains the `m0x1` notation for memory locations.

## Memory management:

This version of KSM contains three methods of memory management:

### Registers: All of the following registers are avalible to use raw in ksm:

- R9
- R10
- R11
- R12
- R13
- R14
- R15

RAX, RBX, etc are *not* avalible, and are used as scratch registers for the compiler.

### Stack: The follow stack operations are avalible:

- push x -> Push x onto the stack. If x is a memory location or register, push the value of that register.
- pop x -> Pop top of stack into memory location / register x.
- peek x -> Place top of stack into memory location / register x without modifying stack.

### Manual memory locations:

The old style `m0x1` style syntax is still avalible; however, additional syntax is also avalible in the form of `[]`. This serves as a sort of offset, eg in c:

`[0x123]` = `*(ksm_mem_pointer + 0x123)`<br>
`[rax]` = `*(ksm_mem_pointer + rax)` <br>
`[m0x123]` = `*(ksm_mem_pointer + *(ksm_mem_pointer + 0x123))`<br>

## Instructions:

Instructions are a string, seperated by one of the following characters:

- newline \n
- semicolon ;

The following instructions are avalible:

- mov dest, src
- - Follows x86 conventions.
<br>

- add dest, src
- - Adds dest and src, result in src.
<br>

- sub dest, src
- mul dest, src
- mod dest, src
- div dest, src
- - See `add`
- shl dest, src
- shr dest, src
- - bitshift dest src bits either left or right
<br>

- cmp arg1, arg2
- - Compare arg1 and arg2, storing result for future jumps.
<br>

- jmp lable
- - Unconditional jump to lable
<br>

- je lable
- - Jump if last cmp had arg1 and arg2 equal
<br>

- jne lable
- - Jump if last cmp was not equal
<br>

- jg lable
- - Jump if last cmp had arg1 greater then arg2
<br>

- jl lable
- - Jump if last cmp had arg1 less then arg2
<br>

- push, pop, peek
- - See Memory management, stack
<br>
- hlt src
- - halt with code from src

- raw_asm {\n `nasm code` \n}
- - This command lets you add raw nasm code into your application for speed purposes. During a `raw_asm` segement, all registers will be avalible for whatever purpose you choose. Whatever is within the curly braces with be explicitly placed into the generated nasm, with two exceptions:
<br>

- - ksm_load dest, src
- - -  This command, when used in a `raw_asm` segment, will load the value from src into the register dest. This can be used to grab values from ksm's 
memory while in a `raw_asm` segment.
<br>

- - ksm_store dest, src
- - -  This command, when used in a `raw_asm` segment, will store the value from the register src into ksm's memory location dest.
<br>
- - This must be used as follows:
```
raw_asm 
{
    commands
}
```
- - The brackets cannot be on the same line as the commands.
<br>

- print_str string
- - Prints a string to stdout.
<br>

- print_int src
- - Prints a number to stdout.
<br>

- print_hex src
- - Prints a number in hex form to stdout.
<br>

- open_file n, dest
- - Opens the nth argument of the program, places fp in dest.
<br>

- fgetc dest, src
- - Using src as the file pointer, place character in dest.
<br>

- feof dest, src
- - Using src as the file pointer, place result of `feof` call in dest.
