from numpy import *
import cmath
# Creating complex numbers
z = -3 -4j
print(z)

# Computing the real and imag parts of the complex number
z_real = real(z)
z_imag = imag(z)
print(f'Real: {z_real}')
print(f'Imag: {z_real}')

#  Computing the module of the complex number
z_mag = sqrt(z_real**2 + z_imag**2)
print(f'Magnitude: {z_mag}')
z_mag_2 = sqrt(z*conj(z))
print(f'Magnitude: {z_mag_2}')
z_mag_3 = abs(z)
print(f'Magnitude: {z_mag_3}')

# Computing the angle of a complex number
z_rad = angle(z)
print(f'Rad: {z_rad:.2f}')
z_deg = angle(z) * 180/pi
print(f'Deg: {z_deg:.2f}')
z_rad_2 = arctan2(z_imag,z_real)
print(f'Deg: {z_rad_2:.2f}')

# |cos(x)| <= 1, this is true only for real numbers.
cos_j = cos(1j)
print(f'cos(j): {cos_j}')

# There are log and ln of negative numbers. They are complex!
ln_minus_one = cmath.log(-1)
log_minus_one = cmath.log10(-1)
print(f'ln(-1): {ln_minus_one}')
print(f'log(-1): {log_minus_one}')
