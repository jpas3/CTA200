# Recall that you have to load the intel compiler module
# module load intel/intel-19
# After you do that, the compiler is called "ifort"
# 
# About modules: https://wiki.cita.utoronto.ca/index.php/Modules
#
#f90 = ifort
avg_world: main.o average.o
	g++ -o xaverage main.o average.o
#
main.o: main.c average.o
	g++ -c main.c
#
average.o: average.c
	g++ -c average.c
#
clean:
	-rm *.o *~ *.mod xaverage
