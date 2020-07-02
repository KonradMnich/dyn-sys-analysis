import numpy as np
#Librarie of the common dynamical systems

class Simple_harmonic_oscillator:
        
    def __init__(self, m = 1, k = 1):
        self.m = m
        self.k = k
        
    def rhs(self, x, t):
        x0 = x[1]
        x1 = -self.k / self.m * x[0]
        return [x0, x1]
    
    
class Damped_harmonic_oscillator:
    
    def __init__(self, m = 1, k = 1, c = 1):
        self.m = m
        self.k = k
        self.c = c
        
    def rhs(self, x, t):
        x0 = x[1]
        x1 = -self.k / self.m * x[0] - self.c / self.m * x[1]
        return [x0, x1]
    
    
class Forced_harmonic_oscillator:
    
    def __init__(self, m = 1, k = 1, c = 1, F = 1, w = 1):
        self.m = m
        self.k = k
        self.c = c
        self.F = F
        self.w = w
        
    def rhs(self, x, t):
        x0 = x[1]
        x1 = -self.k / self.m * x[0] - self.c / self.m * x[1] + \
            self.F * np.sin(self.w * t)
        return [x0, x1]


class Duffing:
    
    def __init__(self, a=-1, b=1, d=0.3, w=1.2, y=0.37):
        self.a = a
        self.b = b
        self.d = d
        self.w = w
        self.y = y
        
    def rhs(self, x, t):
        x0 = x[1]
        x1 = -self.a*x[0] - self.b*x[0]**3 - self.d*x[1] +\
            self.y*np.cos(self.w * t)
        return[x0, x1]
    