from numpy import *
import cmath
import matplotlib.pyplot as plt
#plot function f(t) = sin(2*pi 10t + pi/6)
t = arange(0,0.2-0.2/500,0.2/500)
f = sin(2*pi*10*t+pi/6)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.plot(t,f)
plt.show()

#using others patterns
k = arange(0,100)
w = exp(1j*(pi/100 + 2*pi*k/100))
plt.plot(real(w), imag(w), 'o')
plt.xlabel('Re(w)')
plt.ylabel('Im(w)')
plt.axis('equal')
plt.show()