import numpy as np
import matplotlib.pyplot as plt

n=1087690
c1=0.0
for i in range(n):
    c1=c1+np.sin(i)
c2=0.0
s=0.0 
y=0 
t=0
for i in range(n):
    y=np.sin(i)-s      
    t=c2+y      
    s=(t-c2)-y  
    c2=t
c=0.5*(np.sin(n-1)-(1/np.tan(0.5))*np.cos(n-1)+1/np.tan(0.5))
print(c)
print(c1)
print(c2)