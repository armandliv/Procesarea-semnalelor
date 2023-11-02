import numpy as np
import matplotlib.pyplot as plt
import math

frecventa = 5
def sinusoida(t):
    return np.sin(2*np.pi*frecventa*t)

fv_esnt = 2000
x = np.linspace(0,1,fv_esnt)
y = sinusoida(x)
i=0
yy = np.zeros(fv_esnt,dtype='complex')
for i in range(fv_esnt):
    yy[i] = y[i]*np.exp(-2*np.pi*1j*i/fv_esnt)

plt.plot(x,y)
plt.savefig("Lab3/grafice/2_1.pdf", format="pdf")
plt.savefig("Lab3/grafice/2_1.png", format="png")
plt.show()
plt.scatter(yy.real,yy.imag,c=abs(yy))
plt.savefig("Lab3/grafice/2_2.pdf", format="pdf")
plt.savefig("Lab3/grafice/2_2.png", format="png")
plt.show()

omega = [1,2,5,7]
k=0
for w in omega:
    k+=1
    for i in range(fv_esnt):
        yy[i] = y[i]*np.exp(-2*np.pi*1j*w*i/fv_esnt)
    plt.scatter(yy.real,yy.imag,c=abs(yy))
    plt.savefig(f'Lab3/grafice/2_{2+k}.pdf', format="pdf")
    plt.savefig(f'Lab3/grafice/2_{2+k}.png', format="png")
    plt.show()
