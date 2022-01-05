FFLAGS="-Wall -Wextra -O2 -Wno-unused-dummy-argument"
gfortran -c src/*.f90 $FFLAGS
mv *.o *.mod obj/
gfortran obj/*.o -o output
