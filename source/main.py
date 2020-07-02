import matplotlib.pyplot as plt
from models import *
from tools import Poincare, System_ode

sys = Damped_harmonic_oscillator()

sym = System_ode(sys)


sym.reintegrate(100, [1, 0], 640)
#sym.plot_time_series()
sym.plot_phase_portrait()
#sym.plot_poincare_map(16)