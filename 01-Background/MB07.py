from numpy import *
import cmath
import matplotlib.pyplot as plt
from scipy.signal import residue

A = array([[2,3], [2,5], [0,6]])
print(f"Matriz A: {A}")
B = array([[2,3], [4,5]])
print(f"Matriz B: {B}")
#Residue
R, P, K = residue([1, 0, 0, 0, 0, pi], [1, -sqrt(8), 0, sqrt(32), -4], rtype='min', tol=0.01) 
print(f'R: {R}')
print(f'P: {P}')
print(f'K: {K}')