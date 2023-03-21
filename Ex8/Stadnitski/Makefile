PYTHIA8_DIR = pythia8307

INC = -I$(PYTHIA8_DIR)/include
LIB = -L$(PYTHIA8_DIR)/lib -lpythia8 -ldl
OPT = -g -Wall

all:
	$(MAKE) width

%:
	$(CXX) $(OPT) $(INC) $@.cc $(LIBS) -o $@

clean:
	#rm -rf $(wildcard *~ main* pythia* *.exe)

width:
	$(CXX) $(OPT) $(INC) $@.cc $(LIBS) -o width.exe