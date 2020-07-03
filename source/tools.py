import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class ODE_preview:
    
    def __init__(self, model):
        self.t = []
        self.model = model
        self.x = []
        self.points = []        
        print('system ready')
    
    def solve(self, t_max, x_init, resolution, mute = 0):
        self.t = np.linspace(0, t_max, resolution)
        self.x = odeint(self.model.rhs, x_init, self.t)
        if mute == 0:
            print('state reintegrated')
        
    def plot_phase_portrait(self):
        plt.figure()
        plt.plot(self.x[:,0], self.x[:,1])
        plt.xlabel('x')
        plt.ylabel('dx/dt')
        plt.title('Phase portrait')
        print('phase portrait plotted')
        
    def plot_time_series(self):
        plt.figure()
        plt.plot(self.t, self.x[:,1])
        plt.xlabel('t')
        plt.ylabel('x')
        plt.title('Time series')
        print('time series plotted')
        
    def plot_poincare_map(self, T=6.28):
        T_n = int(round(T/(self.t[1] - self.t[0])))
        index = range(0, len(self.x), T_n)
        plt.figure()
        plt.scatter(self.x[index, 0], self.x[index, 1], s=3)
        plt.xlim([1.1*min(self.x[:,0]), 1.1*max(self.x[:,0])])
        plt.ylim([1.1*min(self.x[:,1]), 1.1*max(self.x[:,1])])
        plt.xlabel('x')
        plt.ylabel('dx/dt')
        plt.title('Poincare map')
        print('poincare map plotted')
        
    def plot_resonance(self, w_lims=[0, 2], resolution=100):
        max_x=[]
        w_range = np.linspace(w_lims[0], w_lims[1], resolution)
        try:
            for w in w_range:
                self.model.w=w
                self.solve(self.t[-1], self.x[1,:], len(self.t), mute=1)
                max_x.append(max(self.x[:,0]))
            
            plt.figure()
            plt.plot(w_range, max_x)
            plt.xlabel('freq. of excitation')
            plt.ylabel('x max')
            plt.title('Resonance plot')
            print('resonance plot ready')
            
        except:
            print('Feature only accessible for the forced systems')
        

