#!/usr/bin/python


import numpy as np
import matplotlib.pyplot as plt

x=167.0
c2=1
i=1
frac=1.0
y=1
c1=np.exp(-167)
while 1/c2-c1>0:
    i=i+1
    frac=frac*i
    y=y*x
    c2=c2+y/frac
print(c1)
print(1/c2)
print(i)
