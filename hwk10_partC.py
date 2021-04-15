#finished by Kay Towner

import numpy as np
import matplotlib.pyplot as plt

G = 6.6738 * np.exp(11) #m^3 kg^-1 s^-2
M = 1.9891 * np.exp(30)#kg  mass of the sun
AU = 1.496e11 #1 astronomical unit in meters
rho = 1 #kilometer per year
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

#FOR PART C:
def run_rk4_adaptive(initial_state=None, initial_h=None, tmax=None):
    """Function for the rk4 adaptive method."""
    r = initial_state
    h = initial_h
    xpoints = []
    ypoints = []
    while t<tmax:
        #Do one large step
        r1 = r + rk4_step(r=r, h=2*h, f=f)
        #Do two small steps
        r2 = r + rk4_step(r=r, h=h, f=f)
        r2 = r2 + rk4_step(r=r2,h=h, f=f)

        #calculate value of rho
        ex = 1/30 * (r - r2)
        ey = 1/30 * (r - r2)
        rho = np.sqrt(ex**2 + ey**2)

        #calculate new values of t, h, r
        #update points if appropriate
        if rho>=1.0:
            t = t/2
            h = h/2
            r = r/2
            xpoints.append(r[0])
            ypoints.append(r[1])
            pass
        else:
            h = h*2
            pass
    return np.array([xpoints, ypoints])

if __name__ == "__main__":
    h0 = 1.0e5 #initial step size
    tmax = 3.0e9 #total time
    e = np.sqrt(ex**2+ey**2) #error value

    delta = 1e3/(365.25*24*3600) #meters accuracy per second

    x0, y0 = 4e12, 0 #starting pos, 4 billion kilometers
    vx0, vy0 = 0, 500 #starting velocity, m/s
    r0 = np.array([x0, y0, vx0, vy0])
    
#running the rk4 adaptive method:
    xpos, ypos = run_rk4_adaptive(initial_state= r0, initial_h= h0, tmax= tmax)
    print("The Positions are:",xpos, ypos)

#rk4step:
    steps = rk4_step(r=r0, h=h0, f=f)
#Make the plot
    plt.plot(xpos/AU, ypos/AU, alpha = 0.5)
    plt.plot(xpos/AU, ypos/AU, 'k.')
#part d:
    plt.scatter(steps) #addingin the rk4steps-dots
    plt.show()
