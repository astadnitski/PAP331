SRC = $(wildcard *.cc)
OBJ = $(addsuffix .o, $(basename $(SRC)))
OPT = -Wall -o

INC = -Iinterface -I$(ROOTSYS)/include
ROOTLIBS = -L$(ROOTSYS)/lib -lCore -lTree -lMathCore -lRIO -lHist -lGpad

all:
	@$(MAKE) compile --no-print-directory
	@$(MAKE) run --no-print-directory
	@$(MAKE) clean --no-print-directory

compile:
	@$(CXX) makenumbers.cc $(INC) $(ROOTLIBS) $(OPT) test0
	@$(CXX) makeplot.cc $(INC) $(ROOTLIBS) $(OPT) test1

run:
	@./test0
	@./test1

clean:
	@rm test0 test1