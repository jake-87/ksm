# The KSM language spec

## part 1: the vm

### registers

there are 8 registers: r1 through r8. They are treated as memory locations for all intents and purposes.
when in binary form, they are 0x1 - 0x8; then other mem continues from there.

### opcodes

Opcodes are formed by a sequence of 8 bytes, like so:

`02 b7 55 00`

The first is the opcode, the other three are operands.

### types of opcodes

If the argument should be left blank, it is signified with zeros.

#### `01 xx 00 00` - halt, return code, null, null

n.a.

#### `02 xx yy zz` - mov, destination, source, mode

mode is one of:

`00` - mem <- mem

`01` - mem <- value

`02` - mem <- stdin

#### `03 xx yy zz` - add, val1, val2, mode
#### `03 xx yy zz` - sub, val1, val2, mode
#### `03 xx yy zz` - mul, val1, val2, mode
Adds/subtracts/multiplys two values and puts result in r1.

mode is one of:

`00` - mem + mem

`01` - mem + value

`02` - value + mem

`03` - value + value

#### `04 xx 00 00` - prt, val1, null, null

Prints a memory cell to stdout.

#### `05 xx yy zz` - jmp, address part 1, ap2, ap3

Jumps to spesified block of memory. Parts are concatenatec to form a full address, like so:

`05 00 41 a4` means `jmp to location 0041a4`
#### `06 xx yy zz` - cmp, val1, val2, mode

Compares two values. See mode table for `add`.

#### `07 xx yy zz` - zjmp, ap1, ap2, ap3

Jumps if last comparison was zero.

#### `08 xx yy zz` - nzjmp, ap1, ap2, ap3

Jumps if last comparison was not zero.

### memory

The VM should have some amount bytes of memory, such that `1024 <= mem_size <= infinity`.
