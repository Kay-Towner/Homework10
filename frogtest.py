#By Kay Towner

print("This method I found online and adjusted it to the equation.")
import math
import numpy as np
import matplotlib.pyplot as plt

#solve: d2 - (dxdt)**2 + x + 5
def dif(t=None, h=None, x=None, dxdt=None, d2 = None):
    """Differential equation to solve.
    d2=leapfrogmethod, dxdt=thederivative=0"""
    return -5 - x

if __name__ == "__main__":
    #VERIABLES:
    h = 0.001 #step size
    t = np.arange(0, 50, h) #time
    x = 1 #initial condition (position)
    dxdt = 0
    
    v = np.empty(int(h+1)) #velocity initial
    x = np.empty(int(h+1))
    x[0] = x
    v[0] = 0
    new = dif(x=x)

    #Leapfrog:
    for i in range(0, int(h+1)):
        old = new
        x[i] = x[i-1] + v[i-1]*h + (1/2)*(old)*h**2
        new = dif(x=i)
        v[i] = v[i-1] + (1/2)*(old + new)*h



        print("test 1 v", v)
        print("test 2 x[i]:", x[i])
    #plt.plot(x, t)#x and y should be the same size
    plt.xlabel('t')
    plt.ylabel('t(x)')
    #plt.show
