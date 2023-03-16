import numpy as np
import os
import re

gamma = re.compile('GammaTot-SMHH')
input = np.loadtxt('var.in', dtype = str)
masses = range(120, 131)
output = ['FeynHiggs decay width calculation', '---']

for mass in masses:

    input[2][1] = mass
    np.savetxt('var.in', input, fmt = '%s')
    os.system('./build/FeynHiggs var.in > output.txt')

    for row, line in enumerate(open('output.txt')):
        for match in re.finditer(gamma, line):
            for num in re.finditer('\d+\.\d+E\-\d+', line):
                print(mass, num.group())
                output.append(str(mass) + '     ' + num.group())

os.system('rm output.txt')
np.savetxt('br.sm2', output, fmt = '%s')