import numpy as np
import matplotlib.pyplot as plt
import math
import time


def s1(t):
    return np.sin(2*np.pi*26*t)

def s2(t):
    return np.sin(2*np.pi*14*t)

def s3(t):
    return np.sin(2*np.pi*6*t)

fig, axs = plt.subplots(4)

x = np.linspace(0,1,1280)
y = s1(x)
axs[0].plot(x,y)


x = np.linspace(0,1,1280)
y = s1(x)
axs[1].plot(x,y)
x = np.linspace(0,1,50)
y = s1(x)
axs[1].scatter(x,y)

x = np.linspace(0,1,1280)
y = s2(x)
axs[2].plot(x,y)
x = np.linspace(0,1,50)
y = s1(x)
axs[2].scatter(x,y)

x = np.linspace(0,1,1280)
y = s3(x)
axs[3].plot(x,y)
x = np.linspace(0,1,50)
y = s1(x)
axs[3].scatter(x,y)

plt.savefig("Lab4/grafice/3.pdf", format="pdf")
plt.savefig("Lab4/grafice/3.png", format="png")
plt.show()