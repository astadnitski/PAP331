PYTHIA8_URL = https://pythia.org/download/pythia83/pythia8307.tgz
PYTHIA8_TGZ = $(notdir $(PYTHIA8_URL))
PYTHIA8_DIR = $(basename $(PYTHIA8_TGZ))

INC = -I$(PYTHIA8_DIR)/include
LIB = -L$(PYTHIA8_DIR)/lib -lpythia8 -ldl
OPT = -g -Wall

all: 
	$(MAKE) getPythia
	#$(MAKE) test

getPythia:
	wget $(PYTHIA8_URL)
	tar xfvz $(PYTHIA8_TGZ)
	cd $(PYTHIA8_DIR) && ./configure && make

test:
	$(CXX) $(OPTl) $(INC) $@.cc $(LIB) -o test.exe
	@echo Now run test.job

clean:
	rm -rf $(wildcard *.tgz *~ *.txt *.exe)
	@echo State reset