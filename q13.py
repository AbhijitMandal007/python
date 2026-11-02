import numpy as np
from scipy.integrate import quad

#function define
def f1(x):
    return x**2 + 12*x +1
def f2(x):
    return np.sin(x)

# derevative at x = x0
x0 = 2
h  = 1e-7

d1 = (f1(x0+h) - f1(x0-h))/(2*h)
d2 = (f2(x0+h) - f2(x0-h))/(2*h)

# intrgration 
integral ,error = quad(f1,0,3)

print("Derivative of f1 at x =",x0,":",round(d1,2),"\n")
print("Derivative of f2 at x =",x0,":",d2,"\n")
print("intrdration from x = 0 to 3 :",integral)
print("error estimate = ",error)