#import matplotlib.pyplot as plt
from models import Forced_harmonic_oscillator
from tools import Poincare

sys = Forced_harmonic_oscillator()

#def poincare(model, x_ini, period = 1, num_of_periods = 100,\
 #            last_periods = 10, resolution = 100):
p = Poincare(sys.rhs, [0, 0] )

p.plot_map(3)