import numpy as np
import matplotlib.pyplot as plt

def sinusoida(t):
    return np.sin(2*np.pi*100*t)

def dreptunghiulara(N):
    return np.ones(N)

def Hanning(N):
    return [0.5*(1-np.cos(2*np.pi*i/N)) for i in range(N)]

N = 200
x = np.linspace(0,1,N)

y = sinusoida(x)
y = y * dreptunghiulara(N)
plt.plot(x,y)
plt.savefig("Lab6/grafice/3_dreptunghiulara.pdf", format="pdf")
plt.savefig("Lab6/grafice/3_dreptunghiulara.png", format="png")
plt.show()

y = sinusoida(x)
y = y * Hanning(N)
plt.plot(x,y)
plt.savefig("Lab6/grafice/3_Hanning.pdf", format="pdf")
plt.savefig("Lab6/grafice/3_Hanning.png", format="png")
plt.show()

