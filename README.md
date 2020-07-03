# dyn-sys-analysis
 
Program containg basic tools for analysis of dynamical systems with two degrees of freedom.
It may be helpful to solve systems of first order ODEs and visualise them via time series,
poincare maps, phase diagrams and maybe more in future.

## dependencies
To use the program you need:
* Python 3
* numpy
* matplotlib
* scipy

## source files
The program consists of:
* main.py
* models.py
* tools.py

## manual
1) The user interacts with the program through the *main.py* script.
2) First, we import the system to be investigated from the module containted in *models.py*. *models.py* has a few common dynamic models defined (such as simple harmonic oscillator or duffing oscillator), but feel free to add your own models following the convention.
3) Next, class ODE_preview is loaded as its instance does all the computations required further on. 
4) After the imports are done we initialise the model and than pass it as an argument to the instance of ODE_preview.
5) Once the objects are ready. We must solve the equations of motion before the visualisations are made.
6) At the end feel free to visualise your model as you wish through the methods of ODE_preview.
