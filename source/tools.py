import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class System_ode:
    def __init__(self, model):
        self.t = []
        self.model = model
        self.x = []
        self.points = []        
        print('system ready')
    
    def reintegrate(self, t_max, x_init, resolution):
        self.t = np.linspace(0, t_max, resolution)
        self.x = odeint(self.model.rhs, x_init, self.t)
        print('state reintegrated')
        
    def plot_phase_portrait(self):
        plt.plot(self.x[:,0], self.x[:,1])
        
        print('phase portrait plotted')
    def plot_time_series(self):
        plt.plot(self.t, self.x[:,1])
        print('time series plotted')
        
    def plot_poincare_map(self, T=1):
        try:
            T=2*math.pi/self.model.w
            T_n = T/(self.t[2] - self.t[1])
        except:
            T_n = T/(self.t[2] - self.t[1])
            T_n = T
        
        index = range(0, len(self.x), T_n)
        plt.scatter(self.x[index, 0], self.x[index, 1])
        print('poincare map plotted')


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
            plt.scatter(self.points[i][0], self.points[i][1],\
                        c = 'blue', s = 2)
            
#class Bifurcation_1D:
