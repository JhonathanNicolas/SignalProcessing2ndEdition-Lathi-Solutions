from numpy import *
import cmath
import matplotlib.pyplot as plt

#Wrapper a function
t = arange(0,0.2-0.2/500,0.2/500)
f = sin(2*pi*10*t+pi/6)
g = exp(-10*t)
h = f*g
plt.plot(t,f, '-k', t,h, ':k')
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.legend(['f(t)', 'h(t)'])
plt.show()