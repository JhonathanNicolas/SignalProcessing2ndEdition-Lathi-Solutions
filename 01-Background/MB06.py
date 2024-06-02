from numpy import *
import cmath
import matplotlib.pyplot as plt

#Creating vectors
r = array([1, 0, 0])
print(f"Vector r: {r}")

#Creating Matrices
A = array([[2,3], [2,5], [0,6]])
print(f"Matriz A: {A}")

#Transposed Matriz
c = transpose(A)
print(f"Transpost Matriz: {c}")

#concatenate
B = concatenate([c,c])
print(f"Concatenated B: {B}")

#Access indexes
print(f"Showing B(0,0): {B[0][0]}")

#Acess Range indexes
print(f"Showing B(0:2,0:2): {B[0:2][0:2]}" )
print(f"Showing B(2:): {B[2:]}" )


#Resolving an equation
A = array([[1, -2, 3],[-sqrt(3), 1 , -sqrt(5)],[3, -sqrt(7), 1]])
y = array([[1], [pi], [exp(1)]])
print(f"A: {A}")
print(f"y: {y}")
x = dot(linalg.inv(A),y)
print(f'x: {x}')
A_sub = A[:, 1:3]
new_matrix = hstack((y, A_sub))
det_new_matrix = linalg.det(new_matrix)
det_A = linalg.det(A)
x1 = det_new_matrix / det_A
print(f'x1: {x1}')

#Creating curves using matrices
alfa = arange(0,10)
alfa = alfa[newaxis, :]
t = arange(0,0.2001,0.001)
T = tile(t[:, newaxis], (1, len(alfa)))
exp_part = exp(-T * alfa)
print(exp_part)
sin_part = sin(2 * pi * 10 * T + pi / 6)
H = exp_part * sin_part
print(f'H: {H}')
plt.plot(t, H)
plt.xlabel('t')
plt.ylabel('h(t)')
plt.show()