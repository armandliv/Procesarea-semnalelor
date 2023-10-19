import numpy as np
import matplotlib.pyplot as plt

def sinus(t,amplitudine,frecventa,faza):
    return amplitudine*np.sin(2*np.pi*frecventa*t+faza)


def plot(start,end,step,functie,amplitudine,frecventa,faza):
    t = start
    xx = []
    yy = []
    while t <= end:
        xx += [t]
        yy += [functie(t,amplitudine,frecventa,faza)]
        t+=step
    plt.plot(xx,yy)

plot(0, 0.03, 0.00001, sinus, 1, 200, 0)
plot(0, 0.03, 0.00001, sinus, 1, 200, np.pi/2)
plot(0, 0.03, 0.00001, sinus, 1, 200, np.pi/3)
plot(0, 0.03, 0.00001, sinus, 1, 200, np.pi/4)
plt.show()


z = np.random.normal(0,1,3001)

t = 0
xx = []
x1 = []
while t <= 0.03:
    xx += [t]
    x1 += [sinus(t,1,200,0)]
    t+=0.00001

t = 0
xx = []
x2 = []
while t <= 0.03:
    xx += [t]
    x2 += [sinus(t,1,200,np.pi/2)]
    t+=0.00001

t = 0
xx = []
x3 = []
while t <= 0.03:
    xx += [t]
    x3 += [sinus(t,1,200,np.pi/3)]
    t+=0.00001

t = 0
xx = []
x4 = []
while t <= 0.03:
    xx += [t]
    x4 += [sinus(t,1,200,np.pi/4)]
    t+=0.00001

def squared_norm2(v):
    s = 0
    for x in v:
        s += x * x
    return s

for snr in [0.1,1,10,100]:
    y = []
    gamma = np.sqrt(squared_norm2(x1)/(snr*squared_norm2(z)))
    for i in range(3001):
        y += [x1[i]+gamma*z[i]]
    plt.plot(xx,y)
    plt.show()

for snr in [0.1,1,10,100]:
    y = []
    gamma = np.sqrt(squared_norm2(x1)/(snr*squared_norm2(z)))
    for i in range(3001):
        y += [x1[i]+gamma*z[i]]
    plt.plot(xx,y)
plt.show()

