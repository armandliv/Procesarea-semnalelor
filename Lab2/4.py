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

fig, axs = plt.subplots(3)
fig.suptitle("Sinus, sawtooth si suma lor") 
fig.tight_layout(pad=3.2)

for ax in axs.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("y")

axs[0].plot(xx,y1)
axs[0].set_title("Sinus")

axs[1].plot(xx,y2)
axs[1].set_title("Sawtooth")

axs[2].plot(xx,y3)
axs[2].set_title("Suma")

plt.savefig("Lab2/grafice/4.pdf", format="pdf")
plt.show()
