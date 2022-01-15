program main
    use parser
    implicit none
    character (len=100) :: filepath, memory
    integer(kind = 8) :: imemory
    if (command_argument_count() /= 2) then
        print *, "Error: Two arguments needed; ./output <filepath> <memory size>"
        call EXIT(1)
    end if
    call get_command_argument(1, filepath)
    call get_command_argument(2, memory)
    read(memory, *) imemory
    call parse(filepath, imemory)
    print *, "Hello World"
end program main