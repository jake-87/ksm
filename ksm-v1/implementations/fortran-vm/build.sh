FFLAGS="-Wall -Wextra -O2 -Wno-unused-dummy-argument"
gfortran -c src/*.f08 $FFLAGS
mv *.o *.mod obj/
gfortran obj/*.o -o output
