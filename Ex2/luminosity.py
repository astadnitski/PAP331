import linecache
import numpy as np
import re

#data = np.loadtxt('brilcalc.log', dtype = '', 'delimiter = '|')

l = 333.333333333

d = re.compile('\|')
p = re.compile('totrecorded')
n = re.compile('\d*\.\d*')

cell = [0, 0]

for row, line in enumerate(open('brilcalc.log')):
    col = 0
    for match in re.finditer(p, line):
        for match in re.finditer(d, line):
            col += 1
        cell = [row + 1, col - 1]

line = linecache.getline('brilcalc.log', cell[0] + 2)
for match in re.finditer(n, line):
    l = float(match.group())

print('Luminosity:', '{:.1f}'.format(l * 1e-3), '/fb')
