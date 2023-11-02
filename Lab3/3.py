import numpy as np
import matplotlib.pyplot as plt
import math

def sinusoida(t,frecventa):
    return np.sin(2*np.pi*frecventa*t)

def semnal(t):
    return sinusoida(t,7)+sinusoida(t,11)+sinusoida(t,13)

fv_esnt = 10000  # pt 100 sau alte nr mici aparea leakage
x = np.linspace(0,1,fv_esnt)
y = semnal(x)
plt.plot(x,y)
plt.savefig("Lab3/grafice/3_1.pdf", format="pdf")
plt.savefig("Lab3/grafice/3_1.png", format="png")
plt.show()

omega = [i for i in range(100)]
k=0
for w in omega:
    k+=1
    yy=0
    for i in range(fv_esnt):
        yy += y[i]*np.exp(-2*np.pi*1j*w*i/fv_esnt)
    plt.stem(w,abs(yy))
plt.savefig("Lab3/grafice/3_2.pdf", format="pdf")
plt.savefig("Lab3/grafice/3_2.png", format="png")
plt.show()
