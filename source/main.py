from models import Forced_harmonic_oscillator
from tools import ODE_preview

# define your system
sys = Forced_harmonic_oscillator()

# pass the system to the ODE_preview object
sym = ODE_preview(sys)

# solve the system before visualisation
sym.solve(100, [1, 0], 10000)

# visualise
sym.plot_time_series()
sym.plot_phase_portrait()
sym.plot_poincare_map()
sym.plot_resonance()