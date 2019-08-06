'''
    Ex.2 da Lista pra P1
'''

import numpy as np
import matplotlib.pyplot as plt

def s_anal(t):
    return t ** 2

def v_anal(t):
    return 2 * t

def main():
    t = -5.0
    s = s_anal(t)
    v = v_anal(t)
    a = 2.0         # derivada de f(x) = 2x
    dt = 0.1        # dado no enunciado
    pos_num = []
    time_num = []
    pos_anal = []
    time_anal = []

    # loop método numérico
    while t <= 5:
        pos_num.append(s)
        time_num.append(t)
        # euler
        s = s + (v * dt)
        v = v + (a * dt)
        # euler cromer
#        v = v + (a * dt)
#        s = s + (v * dt)
        t = t + dt
    
    t = -5.0
    # loop método analítico
    while t <= 5:
        pos_anal.append(s_anal(t))
        time_anal.append(t)
        t = t + dt
    
        
    plt.figure()
    plt.plot(time_num, pos_num, time_anal, pos_anal, 'r--')
    plt.xlabel('t')
    plt.ylabel('s(t)')
    plt.grid(True)
    plt.show()

main()


