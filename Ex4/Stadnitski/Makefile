SRC = $(wildcard *.cc)
OBJ = $(addsuffix .o $(basename $(SRC)))

all:
	@$(MAKE) compile --no-print-directory
	@$(MAKE) run --no-print-directory
	@$(MAKE) clean --no-print-directory

compile: check.o
	@$(CXX) check.o -Wall -o check

run:
	@./check

clean:
	@rm $(wildcard *.o)
