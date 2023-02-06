import linecache
import numpy as np
import re

### Exercise 2 : 2 ###

luminosity = 0

d = re.compile('\|')
p = re.compile('totrecorded')
n = re.compile('\d*\.\d*')

cell = 0

for row, line in enumerate(open('brilcalc.log')):
    for match in re.finditer(p, line): cell = row + 1

line = linecache.getline('brilcalc.log', cell + 2)
for match in re.finditer(n, line):
    luminosity = float(match.group())

print('- Total recorded luminosity:', '{:.1f}'.format(luminosity * 1e-3), '/fb')

### Exercise 2 : 3 ###

runs, compare = [], []
s = re.compile('Summary')
total = 0

for row, line in enumerate(open('brilcalc.log')):
    for match in re.finditer(n, line):
        compare.append(float(match.group()))
    try: runs.append(np.min(compare))
    except:
        for match in re.finditer(s, line): total = np.sum(runs)
    compare = []


print('- Calculated sum of recorded luminosities:', total, '/pb or', total * 1e-3, '/fb')
print('- Difference to expected:', np.abs(total - luminosity))
print('- Results confirmed:', 1e-8 > np.abs(total - luminosity), '\n- Difference in significant figures is small enough that it is likely the result of rounding the 10th digit past the decimal point')
