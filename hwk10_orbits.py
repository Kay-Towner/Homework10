#finished by Kay Towner

import numpy as np
import matplotlib.pyplot as plt

G = 6.6738 * np.exp(11) #m^3 kg^-1 s^-2
M = 1.9891 * np.exp(30)#kg  mass of the sun
AU = 1.496e11 #1 astronomical unit in meters
x = 4 #bill kilometers
y = 0 #bill kilometers

def f(r):
    """derivative function to pass to rk4
    pass state vector r = [x, y, vx, vy]"""
    x, y, vx, vy = r
    rcubed = np.sqrt(x**2 + y**2)**3

    fx = vx #return 1st parameter
    fy = vy #return 2nd parameter
    fvx = -G*M * x/rcubed #return 3rd parameter
    fvy =  -G*M * y/rcubed#return last parameter
    return np.array([fx, fy, fvx, fvy])

def rk4_step(r=None, h=None, f=None):
    """Function of the ranga kata method."""
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    return 1.0/6 * (k1+ 2*k2 + 2*k3 + k4)

def run_rk4_fixed(initial_state=None, initial_h=None, tmax=None):
    """Function for the rk4 fixed method."""
    r = initial_state
    h = initial_h
    xpoints = []
    ypoints = []

    t = 0 #initial time value
    while t<tmax:
        t = t+h #looping adding +h to each pass
        #Do one large step
        r1 = r + rk4_step(r=r, h=2*h, f=f)
        #Do two small steps
        r2 = r + rk4_step(r=r, h=h, f=f)
        r2 = r2 + rk4_step(r=r2,h=h, f=f)
    return np.array([xpoints, ypoints])


if __name__ == "__main__":
    h0 = 1.0e5 #initial step size
    tmax = 1.0e9 #total time
    r = np.sqrt(x**2+y**2) #radius
    
    delta = 1e3/(365.25*24*3600) #meters accuracy per second

    x0, y0 = 4e12, 0 #starting pos, 4 billion kilometers
    vx0, vy0 = 0, 500 #starting velocity, m/s
    r0 = np.array([x0, y0, vx0, vy0])

#testing out the rk4 steps:
    steptest = rk4_step(r=r0, h=h0, f=f)
    print("These are the steps:", steptest)

    fixedrk4test = run_rk4_fixed(initial_state= r, initial_h=h0, tmax= tmax)
    print("These are the rk4 results:", fixedrk4test)

#Making the positions for the rk4 method:
    xpos, ypos = run_rk4_fixed(initial_state= r, initial_h=h0, tmax= tmax)
    
#Make the plot
    plt.plot(xpos/AU, ypos/AU, alpha = 0.5)
    plt.plot(xpos/AU, ypos/AU, 'k.')
    plt.show()
