import numpy as np
import matplotlib.pyplot as plt

def sinus(t,amplitudine,frecventa,faza):
    return amplitudine*np.sin(2*np.pi*frecventa*t+faza)

def cosinus(t,amplitudine,frecventa,faza):
    return amplitudine*np.cos(2*np.pi*frecventa*t+faza)


t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [sinus(t,1,200,0)]
    t+=0.00001
plt.plot(xx,yy)
plt.show()

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [cosinus(t,1,200,-np.pi/2)]
    t+=0.00001
plt.plot(xx,yy)
plt.show()

