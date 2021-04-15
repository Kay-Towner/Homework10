#By Kay Towner

import math
import numpy as np
import matplotlib.pyplot as plt


def dif(t=None, h=None, x=None, dxdt=None, d2 = None):
    """Differential equation to solve.
    d2=leapfrogmethod, dxdt=thederivative=0"""
    return d2 - (dxdt)**2 + x + 5

def frog(t=None, h=None, x=None, f=None):
    "Leapfrog method to run on dif."
    #Had difficulty here:
    x=x
    t=t
    
    x = x(t+(3/2)*h)
    x(t+(1/2)*h)+h*f(x(t+h),t+h)
    t = x(t+2*h)
    x(t+h) + h*f(x(t+(3/2)*h),t+(3/2)*h)
    return x, t

if __name__ == "__main__":
    #VERIABLES:
    t = np.arange(0, 50) #time
    x = 1 #initial condition (position)
    dxdt = 0
    h = 0.001 #step size

    d2 = frog(t=t, h=h, x=x, f=dif)
    leapfrog = dif(t=t, h=h, x=x, dxdt=dxdt, d2=d2)

    print(leapfrog)


