from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

class system:
    def __init__(self, k, m):
        self.k = k
        self.m = m
    
    def dxdt(self, x, t):
        x0 = x[1]
        x1 = -self.k / self.m * x[0]
        return [x0, x1]

s1 = system(1,1)
t = np.linspace(1,10,100)
x_ini = [1, 0]

result = odeint(s1.dxdt, x_ini, t)
plt.plot(t, result[:,1])



