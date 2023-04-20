INC = -Iinterface -I$(ROOTSYS)/include
LIB = -ldl
OPT = -g -Wall
ROOTLIBS = -L$(ROOTSYS)/lib -lCore -lTree -lMathCore -lRIO -lHist -lGpad

all: 
	$(MAKE) compile
	$(MAKE) clean

compile:
	@$(CXX) $(OPT) $(INC) analysis.cc $(LIB) $(ROOTLIBS) -o analysis.exe
	@./analysis.exe

clean:
	rm -rf $(wildcard *~ *.txt *.exe)
	@echo State reset