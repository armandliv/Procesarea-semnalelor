import numpy as np
import matplotlib.pyplot as plt

def sinus(t,frecventa):
    return np.sin(2*np.pi*frecventa*t)

def sawtooth(t,frecventa):
    return t*frecventa-np.floor(t*frecventa)

t = 0
xx = []
y1 = []
y2 = []
y3 = []
while t <= 0.02:
    xx += [t]
    y1 += [sinus(t,240)]
    y2 += [sawtooth(t,240)]
    y3 += [sinus(t,240)+sawtooth(t,240)]
    t+=0.000025

plt.plot(xx,y1)
plt.show()
plt.plot(xx,y2)
plt.show()
plt.plot(xx,y3)
plt.show()
