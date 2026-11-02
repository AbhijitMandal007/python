import numpy as np
from scipy.optimize import minimize

def f(v):
    x,y =v
    return (x-2)**2 + (y-2)**2

result = minimize(f,x0=[0,0])

print(",minimum value of x,y = ",result.x)
print(",minimum value of function = ",result.fun)
