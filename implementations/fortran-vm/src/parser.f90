module parser
    use ops
    contains
        subroutine call_ops(op, cpu, a1, a2, a3, concat)
            type(cpu_t), intent(inout) :: cpu
            integer(kind = 8), intent(in) :: op, a1, a2, a3, concat
            select case (op)
            case(0)
                call op00(cpu, a1, a2, a3)
            case(1)
                call op01(cpu, a1, a2, a3)
            case(2)
                call op02(cpu, a1, a2, a3)
            case(3)
                call op03(cpu, a1, a2, a3)
            case(4)
                call op04(cpu, a1, a2, a3)
            case(5)
                call op05(cpu, a1, a2, a3)
            case(6)
                call op06(cpu, a1, a2, a3)
            case(7)
                call op07(cpu, a1, a2, a3)
            case(8)
                call op08(cpu, concat)
            case(9)
                call op09(cpu, concat)
            case(10)
                call op0a(cpu, concat)
            case(11)
                call op0b(cpu, a1, a2, a3)
            case(12)
                call op0c(cpu, a1, a2, a3)
            case(13)
                call op0d(cpu, a1, a2, a3)
            case(14)
                call op0e(cpu, concat)
            case(15)
                call op0f(cpu, concat)
            case(16)
                call op10(cpu, a1, a2, a3)
            case(17)
                call op11(cpu, a1, a2, a3)
            case(18)
                call op12(cpu, a1, a2, a3)
            case(19)
                call op13(cpu, a1, a2, a3)
            case(20)
                call op14(cpu, a1, a2, a3)
            case(21)
                call op15(cpu, a1, a2, a3)
            case(22)
                call op16(cpu, concat)
            case(23)
                call op17(cpu, a1, a2, a3)
            case(24)
                call op18(cpu, a1, a2, a3)
            case default
                print *, "unreachable"
            end select
        end subroutine call_ops
        subroutine parse(filepath, memory)
            character(*), intent(in) :: filepath
            integer(kind = 8), intent(in) :: memory
            integer(kind = 8) :: iop, ia1, ia2, ia3, iconcat
            integer :: iostat, count
            type(cpu_t) :: cpu
            character(len = 2) :: op, a1, a2, a3
            character(len = 6) :: concat
            allocate(cpu%mem(memory))
            open(1, file = filepath, status='old')  
            cpu%
            do while(1 == 1)
                read(1, "(4A)", advance="no", iostat=iostat) op, a1, a2, a3
                concat = a1 // a2 // a3
                print *, op, " ", a1, " ",a2," ", a3, " ", concat
                count = count + iostat
                read(op, "(Z2)", iostat=iostsat) iop
                count = count + iostat
                read(a1, "(Z2)", iostat=iostsat) ia1
                count = count + iostat
                read(a2, "(Z2)", iostat=iostsat) ia2
                count = count + iostat
                read(a3, "(Z2)", iostat=iostsat) ia3
                count = count + iostat
                read(concat, "(Z6)", iostat=iostsat) iconcat
                count = count + iostat
                if (count /= 0) then
                    print *, "Unexpected EOF"
                    call EXIT(1)
                else
                    call call_ops(iop, cpu, ia1, ia2, ia3, iconcat)
                    print *, cpu%mem
                end if
            end do
        end subroutine parse
end module parser