SRC = $(wildcard src/*.cc)
OBJ = $(addsuffix .o, $(basename $(SRC)))

all:
	@$(MAKE) compile --no-print-directory
	@$(MAKE) run --no-print-directory
	@$(MAKE) clean --no-print-directory

compile: $(OBJ)
	@$(CXX) $(OBJ) -Wall -o test

run:
	@./test

clean:
	@rm $(wildcard src/*.o)
