import numpy as np
import matplotlib.pyplot as plt
import sounddevice

def sinus(t,frecventa):
    return np.sin(2*np.pi*frecventa*t)

t = 0
xx = []
yy = []
while t < 0.1:
    xx += [t]
    yy += [sinus(t,240)]
    t+=0.000025

t = 0
while t <= 0.2:
    xx += [t+0.1]
    yy += [sinus(t,400)]
    t+=0.000025

plt.plot(xx,yy)
plt.savefig("Lab2/grafice/5.pdf", format="pdf")
plt.show()

sounddevice.play(yy, 2400)
sounddevice.wait()

# Sunetele se aud la inceput mai lent, iar ulterior se aud mai des, intrucat frecventa este mai mare in partea a 2-a.