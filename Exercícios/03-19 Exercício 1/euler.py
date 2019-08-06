#!/usr/bin/env python3

import math

def main():
    x0 = 2
    t1 = 5
    t2 = 20
    dt = 0.00001
    a = 1.5
    b = 2

    x = x0
    t = 0
    e = 0

    while t < t1:
        x = x + dt * (2*a*t + b)
        e = x - (a*t*t + b*t + x0)
        t += dt

    while t < t2:
        if t - math.floor(t) > 1 - dt:
            print("x({t})\t= {x}\twith {e} error".format(t=t, x=x, e=e))
        x = x + dt * (2*a*t + b)
        # e = x - (x0 + b*t + a*(t*t)/2)
        e = x - (a*t*t + b*t + x0)
        t += dt

if __name__ == "__main__":
    main()