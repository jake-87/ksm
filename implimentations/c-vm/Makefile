CARGS += -O2 -Wall -Wextra -Wpedantic -Wno-unused-parameter
CARGS += -Wno-unused-parameter -Wno-stringop-truncation
PHONY:
	clear
	make com
com:
	cc src/*.c -o output $(CARGS)
	rm -rf tmp
clean:
	rm output
