import numpy as np
import matplotlib.pyplot as plt

def sinus(t,amplitudine,frecventa,faza):
    return amplitudine*np.sin(2*np.pi*frecventa*t+faza)

def cosinus(t,amplitudine,frecventa,faza):
    return amplitudine*np.cos(2*np.pi*frecventa*t+faza)

fig, axs = plt.subplots(2)
fig.suptitle("Semnale sinusoidale: sinus si cosinus") 
fig.tight_layout(pad=2.5)

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [sinus(t,1,200,0)]
    t+=0.00001
axs[0].plot(xx,yy)

t = 0
xx = []
yy = []
while t <= 0.03:
    xx += [t]
    yy += [cosinus(t,1,200,-np.pi/2)]
    t+=0.00001
axs[1].plot(xx,yy)

for ax in axs.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("y")

plt.savefig("Lab2/grafice/1.pdf", format="pdf")
plt.show()

