SRC = $(wildcard *.cc)
OBJ = $(addsuffix .o, $(basename $(SRC)))
OPT = -O -Wall -fPIC

# FROM Example 6-3
ROOTINC := $(shell root-config --cflags)
ROOTLIBS := $(shell root-config --glibs)
INC = -I. $(ROOTINC)
LIBS = -L. -lEvent $(ROOTLIBS)

all:
	@$(MAKE) compile --no-print-directory
	@$(MAKE) run --no-print-directory
	@$(MAKE) clean --no-print-directory

compile: $(OBJ)
	@$(CXX) $(OBJ) $(OPT)
	#root-config --cxx --cflags -o RootExample RootExample.cpp root-config --glibs

run:
	@a.out

clean:
	@rm $(wildcard *.o)
