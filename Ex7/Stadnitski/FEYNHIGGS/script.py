# This script is run from the FeynHiggs-2.18.1 directory

import numpy as np
import os
import re

gamma = re.compile('GammaTot-A0')
input = np.loadtxt('var.in', dtype = str)
masses = range(120, 131)
output = ['FeynHiggs decay width calculation', '---']

for MA0 in masses:

    input[2][1] = MA0
    np.savetxt('var.in', input, fmt = '%s')
    os.system('./build/FeynHiggs var.in > output.txt')

    for row, line in enumerate(open('output.txt')):
        for match in re.finditer(gamma, line):
            for num in re.finditer('\d+\.\d+E\-\d+', line):
                output.append(str(MA0) + '     ' + num.group())

os.system('rm output.txt')
np.savetxt('br.sm2', output, fmt = '%s')