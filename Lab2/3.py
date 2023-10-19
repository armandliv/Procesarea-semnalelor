import scipy.io.wavfile
import scipy.signal
import sounddevice
import numpy as np
import matplotlib.pyplot as plt


# a
def sinusoida(t,frecventa):
    return np.sin(2*np.pi*frecventa*t)

t = 0
xx = []
y1 = []
while t <= 1:
    xx += [t]
    y1 += [sinusoida(t,400)]
    t+=0.000625

# b

t = 0
xx = []
y2 = []
while t <= 3:
    xx += [t]
    y2 += [sinusoida(t,800)]
    t+=0.000025


# c

def sawtooth(t,frecventa):
    return t*frecventa-np.floor(t*frecventa)


t = 0
xx = []
y3 = []
while t <= 1:
    xx += [t]
    y3 += [sawtooth(t,240)]
    t+=0.000025



# d

def square(t,frecventa):
    return np.sign((np.mod(np.floor(t*frecventa),2)-0.5)*(-1))



t = 0
xx = []
y4 = []
while t <= 1:
    xx += [t]
    y4 += [square(t,300)]
    t+=0.000025


sounddevice.play(y1, 1600)
sounddevice.wait()
sounddevice.play(y2, 120000)
sounddevice.wait()
sounddevice.play(y3, 40000)
sounddevice.wait()
sounddevice.play(y4, 40000)
sounddevice.wait()

yyy = np.array(y1)

rate = 1600
scipy.io.wavfile.write('Lab2/sinusoida.wav', rate, yyy)

rate, x = scipy.io.wavfile.read('Lab2/sinusoida.wav')
sounddevice.play(x,rate)
sounddevice.wait()