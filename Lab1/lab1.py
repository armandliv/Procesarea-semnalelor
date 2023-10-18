#%%
import numpy as np
import matplotlib.pyplot as plt
#%% ex1
def x(t):
    return np.cos(520*np.pi*t + np.pi/3)

def y(t):
    return np.cos(280*np.pi*t - np.pi/3)

def z(t):
    return np.cos(120*np.pi*t + np.pi/3)

t = 0
while t<=0.03:
    print(x(t),y(t),z(t))
    t+=0.0005


plt.xlabel("t")
plt.ylabel("x(t)")

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [x(t)]
    t+=0.0005
plt.stem(xx,yy)
plt.show()

plt.xlabel("t")
plt.ylabel("x(t)")
plt.plot(xx,yy)
plt.show()

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [y(t)]
    t+=0.0005
plt.xlabel("t")
plt.ylabel("y(t)")
plt.stem(xx,yy)
plt.show()

plt.xlabel("t")
plt.ylabel("y(t)")
plt.plot(xx,yy)
plt.show()


t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [z(t)]
    t+=0.0005
plt.xlabel("t")
plt.ylabel("z(t)")
plt.stem(xx,yy)
plt.show()

plt.xlabel("t")
plt.ylabel("z(t)")
plt.plot(xx,yy)
plt.show()



t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [x(t)]
    t+=0.006
plt.xlabel("t")
plt.ylabel("x(t)")
plt.stem(xx,yy)
plt.show()

plt.xlabel("t")
plt.ylabel("x(t)")
plt.plot(xx,yy)
plt.show()

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [y(t)]
    t+=0.006
plt.xlabel("t")
plt.ylabel("y(t)")
plt.stem(xx,yy)
plt.show()

plt.xlabel("t")
plt.ylabel("y(t)")
plt.plot(xx,yy)
plt.show()

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [z(t)]
    t+=0.006
    plt.xlabel("t")
    plt.ylabel("z(t)")
plt.stem(xx,yy)
plt.show()

plt.xlabel("t")
plt.ylabel("z(t)")
plt.plot(xx,yy)
plt.show()

xx2=xx
yy2=yy

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [z(t)]
    t+=0.0005
plt.xlabel("t")
plt.ylabel("z(t)")
plt.plot(xx,yy)
plt.stem(xx2,yy2)
plt.show()

plt.xlabel("t")
plt.ylabel("z(t)")
plt.plot(xx,yy)
t = 0
while t <= 0.03:
    plt.scatter(t,z(t))
    t+=0.006
plt.show()

#%% ex2



# a


def sinusoida(t,frecventa):
    return np.sin(2*np.pi*frecventa*t)

t = 0
xx = []
yy = []
while t <= 0.05:
    xx += [t]
    yy += [sinusoida(t,400)]
    t+=0.000025

plt.plot(xx,yy)
plt.show()

t = 0
xx = []
yy = []
while t <= 1:
    xx += [t]
    yy += [sinusoida(t,400)]
    t+=0.000625

plt.plot(xx,yy)
plt.stem(xx,yy)
plt.show()


# b

t = 0
xx = []
yy = []
while t <= 0.01:
    xx += [t]
    yy += [sinusoida(t,800)]
    t+=0.000025

plt.plot(xx,yy)
plt.show()



t = 0
xx = []
yy = []
while t <= 3:
    xx += [t]
    yy += [sinusoida(t,800)]
    t+=0.000025

plt.plot(xx,yy)
plt.show()


# c

def sawtooth(t,frecventa):
    return t*frecventa-np.floor(t*frecventa)

t = 0
xx = []
yy = []
while t <= 0.050025:
    xx += [t]
    yy += [sawtooth(t,240)]
    t+=0.000025

plt.plot(xx,yy)
plt.show()


t = 0
xx = []
yy = []
while t <= 1:
    xx += [t]
    yy += [sawtooth(t,240)]
    t+=0.000025

plt.plot(xx,yy)
plt.show()



# d

def square(t,frecventa):
    return np.sign((np.mod(np.floor(t*frecventa),2)-0.5)*(-1))



t = 0
xx = []
yy = []
while t <= 0.05:
    xx += [t]
    yy += [square(t,300)]
    t+=0.000025

plt.plot(xx,yy)
plt.show()


t = 0
xx = []
yy = []
while t <= 1:
    xx += [t]
    yy += [square(t,300)]
    t+=0.000025

plt.plot(xx,yy)
plt.show()


# e

semnal2D = np.random.rand(128,128)
plt.imshow(semnal2D)
plt.show()

# f

semnal2 = np.zeros((128,128))
for x in range(128):
    for y in range(128):
        semnal2[x][y] = x+y
plt.imshow(semnal2)
plt.show()


#%% 3

# a

### 2000 Hz inseamna 2000 de esantioane intr-o secunda, deci se va face cate un esantion la fiecare 1s/2000 = 0.0005s.
### Deci intre 2 esantioane consecutive este un intervald e timp de 0.0005s.

# b

### 2000 de esantioane intr-o secunda => 2000 * 60 * 60 = 7200000 de esantioane intr-o ora. Fiecare avand 4 biti, 
### acestea vor ocupa 7200000 * 4b = 28800000b = 3600000B = 3.4332275390625 MB
 

















