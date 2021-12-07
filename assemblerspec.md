# KSM Assembler spec

## Memory and literals:

Memory locations should be spesified with a m before either hex or dec literal:

`m0x10` or `m12`

Literals should not:

`0x10` or `12`

## Truth Table

|       | Ag1 | Ag2 |
|-------|-----|-----|
| Pos 1 | Mem | Mem |
| Pos 2 | Mem | Lit |
| Pos 3 | Lit | Lit |

Note how if Ag1 is a Literal, Ag1 cannot be a memory location.

## Opcodes:

mov des src : Where des is a memory location, and src is either a literal or a memory location.

inc src     : Where src is a memory location

dec src     : Where src is a memory location

add ag1 ag2 : Result in m0x1. See Truth table for logic.

sub ag1 ag2 : Result in m0x1. See Truth table for logic.

mul ag1 ag2 : Result in m0x1. See Truth table for logic.

div ag1 ag2 : Result in m0x1. See Truth table for logic.

cmp ag1 ag2 : Compares two values, and stores result for later jmp instructions. See Truth table for logic.

jmp lable   : Jumps to label, spesified like so:

```label_containing-no=spaces:```

Any char is allowed except whitespace.

jmpz lable  : Jumps if last cmp was zero.

jmpnz lable : Jumps if last cmp was not zero.

write ag1   : Writes to screen, can be either memory location or literal.

read ag1    : Reads a number into ag1.

hlt ag1     : Halt with return code ag1, can be memory or literal.

store ag1   : Stores content of m0x1 into memory address ag1, which is a hex number less then 0xFFFFFF.

load ag1    : Loads content of memory location ag1, which is a hex number less then 0xFFFFFF into m0x1.

xor ag1 ag2 : Xor ag1 with ag2, result in m0x1. See Truth table for logic.

and ag1 ag2 : And ag1 with ag2, result in m0x1. See Truth table for logic.

or ag1 ag2  : or ag1 with ag2, result in m0x1. See Truth table for logic.

not ag1     : Not ag1, result in m0x1. See Truth table for logic.

bsl ag1 ag2 : bitshift ag1 ag2 bits left. ag1 must be a memory location, ag2 can be mem or literal.

bsr ag1 ag2 : bitshift ag1 ag2 bits right. ag1 must be a memory location, ag2 can be mem or literal.

movl ag1    : Move ag1, a literal less then 0xFFFFFF, into m0x1

lfa ag1 ag2 : Move content of memory location spesified by value of ag2 into ag2, eg:

`lfa m0x01 m0x03, if 03 contains the value 05, moves the value of memory location 05 into 01.`

lta ag1 ag2 : Move content of memory location ag2 into memory location spesified by ag1, eg:

`lta m0x01 m0x03, if 03 contains the value 05, moves the value of memory location 05 into 01.`
