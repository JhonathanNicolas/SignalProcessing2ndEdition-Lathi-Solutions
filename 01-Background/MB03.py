from numpy import *

#Creating the vector 0:2:11
k = arange(0,11,2)
print(f'Vector {k}')

#Creating vectiong with fractional valuers
k_2 = arange(11.0, 0.0, -10/3)
print(f'Vector {k_2}')

#If the step value is not passed the value "one" is considered
k_3 = arange(0,12)
print(f'Vector: {k_3}')

# Cubic root
k = arange(0,2)
w = exp(1j*(pi/3 + 2*pi*k/3))
print(f'W: {w}')

#solution of 100 roots
k = arange(0,100)
w = exp(1j*(pi/100 + 2*pi*k/100))
print(f'w(5): {w[4]}')

#function f(t) = sin(2*pi 10t + pi/6)
t = arange(0,0.2-0.2/500,0.2/500)
f = sin(2*pi*10*t+pi/6)
print(f"f(1): {f[0]}")