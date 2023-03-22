PYTHIA8_DIR = pythia8307

INC = -I$(PYTHIA8_DIR)/include
LIB = -L$(PYTHIA8_DIR)/lib -lpythia8 -ldl
OPT = -g -Wall

all: 
	$(MAKE) $(PYTHIA8_DIR)

%:
	cp $(PYTHIA8_DIR)/examples/$@.cc .
	$(CXX) $(OPT) $(INC) $@.cc $(LIB) -o $@

list:
	$(CXX) $(OPT) $(INC) $@.cc $(LIB) -o test.exe
	@echo Now run savelist.job

clean:
	@#rm -rf $(wildcard *~ main* pythia* *.exe)
	rm -rf $(wildcard *~ *.txt *.exe)
	@echo State reset
