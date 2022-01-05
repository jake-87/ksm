module ops
    type cpu_t
        integer(kind = 8), dimension(:), allocatable :: mem
        integer(kind = 8) :: cmp
    end type cpu_t
    contains
    subroutine op00(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(a1) = cpu%mem(a2)
        else
            cpu%mem(a1) = a2
        end if
    end subroutine op00

    subroutine op01(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        cpu%mem(a1) = cpu%mem(a1) + 1
    end subroutine op01

    subroutine op02(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        cpu%mem(a1) = cpu%mem(a1) - 1
    end subroutine op02

    subroutine op03(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = cpu%mem(a1) + cpu%mem(a2)
        else if (a3 == 2) then
            cpu%mem(1) = cpu%mem(a1) + a2
        else
            cpu%mem(1) = a1 + a2
        end if
    end subroutine op03

    subroutine op04(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = cpu%mem(a1) - cpu%mem(a2)
        else if (a3 == 2) then
            cpu%mem(1) = cpu%mem(a1) - a2
        else
            cpu%mem(1) = a1 - a2
        end if
    end subroutine op04

    subroutine op05(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = cpu%mem(a1) * cpu%mem(a2)
        else if (a3 == 2) then
            cpu%mem(1) = cpu%mem(a1) * a2
        else
            cpu%mem(1) = a1 * a2
        end if
    end subroutine op05

    subroutine op06(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = cpu%mem(a1) / cpu%mem(a2)
        else if (a3 == 2) then
            cpu%mem(1) = cpu%mem(a1) / a2
        else
            cpu%mem(1) = a1 / a2
        end if
    end subroutine op06

    subroutine op07(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%cmp = cpu%mem(a1) - cpu%mem(a2)
        else if (a3 == 2) then
            cpu%cmp = cpu%mem(a1) - a2
        else
            cpu%cmp = a1 - a2
        end if
    end subroutine op07

    subroutine op08(cpu, concat)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: concat
        cpu%mem(0) = concat / 4
    end subroutine op08

    subroutine op09(cpu, concat)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: concat
        if (cpu%cmp .ne. 0) then
            cpu%mem(0) = concat / 4
        end if
    end subroutine op09

    subroutine op0a(cpu, concat)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: concat
        if (cpu%cmp == 0) then
            cpu%mem(0) = concat / 4
        end if
    end subroutine op0a

    subroutine op0b(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a2 == 1) then
            write (*,'(Z3)') cpu%mem(a1)
        else
            write (*,'(Z3)') a1
        end if
    end subroutine op0b

    subroutine op0c(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        write(*, "(A)", advance="no") ">"
        read "(Z10)", cpu%mem(a1)
    end subroutine op0c

    subroutine op0d(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a2 == 1) then
            call EXIT(cpu%mem(a1))
        else
            call EXIT(a1)
        end if
    end subroutine op0d

    subroutine op0e(cpu, concat)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: concat
        cpu%mem(concat) = cpu%mem(1)
    end subroutine op0e

    subroutine op0f(cpu, concat)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: concat
        cpu%mem(1) = cpu%mem(concat)
    end subroutine op0f

    subroutine op10(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = xor(cpu%mem(a1) , cpu%mem(a2))
        else if (a3 == 2) then
            cpu%mem(1) = xor(cpu%mem(a1) , a2)
        else
            cpu%mem(1) = xor(a1 , a2)
        end if
    end subroutine op10

    subroutine op11(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = and(cpu%mem(a1) , cpu%mem(a2))
        else if (a3 == 2) then
            cpu%mem(1) = and(cpu%mem(a1) , a2)
        else
            cpu%mem(1) = and(a1 , a2)
        end if
    end subroutine op11

    subroutine op12(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = or(cpu%mem(a1) , cpu%mem(a2))
        else if (a3 == 2) then
            cpu%mem(1) = or(cpu%mem(a1) , a2)
        else
            cpu%mem(1) = or(a1 , a2)
        end if
    end subroutine op12

    subroutine op13(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = not(cpu%mem(a1))
        else
            cpu%mem(1) = not(a1)
        end if
    end subroutine op13

    subroutine op14(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = ishft(cpu%mem(a1) , cpu%mem(a2))
        else if (a3 == 2) then
            cpu%mem(1) = ishft(cpu%mem(a1) , a2)
        else
            cpu%mem(1) = ishft(a1 , a2)
        end if
    end subroutine op14

    subroutine op15(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(1) = ishft(cpu%mem(a1) , 0 - cpu%mem(a2))
        else if (a3 == 2) then
            cpu%mem(1) = ishft(cpu%mem(a1) , 0 - a2)
        else
            cpu%mem(1) = ishft(a1 , 0 - a2)
        end if
    end subroutine op15

    subroutine op16(cpu, concat)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: concat
        cpu%mem(1) = concat
    end subroutine op16

    subroutine op17(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        cpu%mem(a1) = cpu%mem(cpu%mem(a2))
    end subroutine op17

    subroutine op18(cpu, a1, a2, a3)
        type(cpu_t), intent(inout) :: cpu
        integer(kind = 8), intent(in) :: a1, a2, a3
        if (a3 == 1) then
            cpu%mem(cpu%mem(a1)) = cpu%mem(a2)
        else
            cpu%mem(cpu%mem(a1)) = a2
        end if
    end subroutine op18
end module ops 