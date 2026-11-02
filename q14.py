import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Given Data
x  = np.array([1,2,3,4,5,6])
y  = np.array([6,17,34,57,86,121])

#define polynomial
def polynomial(x,a,b,c):
    return a*x**2 + b*x + c

coefficients ,covarience = curve_fit(polynomial, x,y)

a,b,c = coefficients
# Polynomial coeffiient
print("polynomial coefficient :")
print("a = ",round(a,2))
print("b = ",round(b,2))
print("c = ",round(c,2))

x_fit = np.linspace(min(x),max(x),100)
y_fit = polynomial(x_fit,a,b,c)

plt.scatter(x,y,label="original data")
plt.plot(x_fit,y_fit,label="fitted curve")
plt.xlabel("x")
plt.ylabel("y")
plt.title("second degree polynomal")
plt.legend()
plt.grid()
plt.show()

print(covarience)


