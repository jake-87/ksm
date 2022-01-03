CARGS += -O2 -Wall -Wextra -pedantic -Wno-unused-parameter
CARGS += -Wno-unused-parameter -Wno-stringop-truncation -Wno-string-concatenation -Wno-newline-eof
CARGS += -Wno-unknown-warning-option
PHONY:
	clear
	make com
com:
	cc src/*.c -o output $(CARGS)
clean:
	rm output
