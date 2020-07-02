import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

'''
def poincare(model, x_ini, period = 1, num_of_periods = 100,\
             last_periods = 10, resolution = 100):
    T = period
    n = num_of_periods
    l = last_periods
    r = resolution
    
    t = np.linspace(0, n * T, r * n)
    x = odeint(model, x_ini, t)
    x.tolist()
    
    points = []
    for i in range(0, l):
        points.append(x[-1 - l * r])
    
    return points '''

class Poincare:
    
    def __init__(self, model, x_ini, period = 1, num_of_periods = 100,\
             resolution = 100):
        
        T = period
        n = num_of_periods
        r = resolution
        
        t = np.linspace(0, n * T, r * n)
        x = odeint(model, x_ini, t)
        x.tolist()
        
        self.points = []
        for i in range(0, n):
            self.points.append(x[0 + i * r])
            
    def plot_map(self, last_periods):
        for i in range(0, last_periods):
            plt.scatter(self.points[i][0], self.points[i][1])
            