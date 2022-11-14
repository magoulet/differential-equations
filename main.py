import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.constants import g
from scipy.integrate import odeint


def equation1():
    def dy_dt(y, t, k):
        return -k * y

    # Initial conditions
    y_0 = 2
    k1 = 0.1
    k2 = 0.4
    k3 = 0.7
    t = np.linspace(0, 20)

    y1 = odeint(dy_dt, y_0, t, args=(k1,))
    y2 = odeint(dy_dt, y_0, t, args=(k2,))
    y3 = odeint(dy_dt, y_0, t, args=(k3,))

    plt.plot(t, y1, 'r', linewidth=2, label=f"k={k1}")
    plt.plot(t, y2, 'b', linewidth=2, label=f"k={k2}")
    plt.plot(t, y3, 'g', linewidth=2, label=f"k={k3}")
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

def equation2():
    def dy_dt(y, t):
        return (-y +1)

    y_0 = 0
    t = np.linspace(0, 5)

    y = odeint(dy_dt, y_0, t)

    plt.plot(t, y, 'r', linewidth=2, label=f"equation 2")
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

def equation3():
    def dy2_dt2():
        return -g

    def dy_dt(y, t, v0):
        return dy2_dt2()*t + v0

    y_0 = 0
    t = np.linspace(0, 5)

    v01 = 20
    v02 = 15
    v03 = 10
    y1 = odeint(dy_dt, y_0, t, args=(v01,))
    y2 = odeint(dy_dt, y_0, t, args=(v02,))
    y3 = odeint(dy_dt, y_0, t, args=(v03,))

    plt.plot(t, np.clip(y1, 0, None), 'r', linewidth=2, label=f"equation 3, v0={v01}")
    plt.plot(t, np.clip(y2, 0, None), 'b', linewidth=2, label=f"equation 3, v0={v02}")
    plt.plot(t, np.clip(y3, 0, None), 'g', linewidth=2, label=f"equation 3, v0={v03}")
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()

def equation4():
    # TODO: add air resistance term, proportional to velocity squared
    def dy2_dt2():
        return -g

    def dy_dt(y, t, vy0):
        return dy2_dt2()*t + vy0

    def dx_dt(y, t, vx0):
        return vx0

    x_0 = 0
    y_0 = 10
    v0 = 20
    theta = math.radians(20)

    vx0 = v0 * math.cos(theta)
    vy0 = v0 * math.sin(theta)
    t = np.linspace(0, 5, 100)

    # x = odeint(dx_dt, x_0, t, args=(vx0,))
    x = vx0*t + x_0
    y = odeint(dy_dt, y_0, t, args=(vy0,))

    plt.plot(x, np.clip(y, 0, None), 'r', linewidth=2, label=f"equation 4, v0={v0}, theta={math.degrees(theta)}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 50)
    plt.ylim(0, 20)
    plt.legend()
    plt.show()


def main():
    # equation1()
    # equation2()
    # equation3()
    equation4()
    return None

if __name__ == '__main__':
    main()

