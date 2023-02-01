from multiprocessing import Process
import numpy as np
import os
import random

def hello(num, i):
    os.system('./hello ' + str(num))
    np.savetxt('pyOut/pyOut' + str(i) + '.txt', ['Hello ' + str(num)], fmt = '%s')

for i in range(10): Process(target = hello, args = (random.randint(0, 9), i)).start()
