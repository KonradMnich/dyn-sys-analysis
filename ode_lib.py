import numpy as np
#Librarie of the common dynamical systems

class Simple_harmonic_oscillator:
    m = 1
    k = 1
        
    def __init__(self, m, k):
        self.m = m
        self.k = k
        
    def rhs(self, x, t):
        x0 = x[1]
        x1 = -self.k / self.m * x[0]
        return [x0, x1]
    
    
class Damped_harmonic_oscillator:
    m = 1
    k = 1
    c = 1
    
    def __init__(self, m, k, c):
        self.m = m
        self.k = k
        self.c = c
        
    def rhs(self, x, t):
        x0 = x[1]
        x1 = -self.k / self.m * x[0] - self.c / self.m * x[1]
        return [x0, x1]
    
    
class Forced_harmonic_oscillator:
    m = 1
    k = 1
    c = 1
    F = 1
    w = 1
    
    def __init__(self, m, k, c, F, w):
        self.m = m
        self.k = k
        self.c = c
        
    def rhs(self, x, t):
        x0 = x[1]
        x1 = -self.k / self.m * x[0] - self.c / self.m * x[1] + \
            self.F * np.sin(self.w * t)
        return [x0, x1]