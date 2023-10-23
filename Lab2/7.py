import numpy as np
import matplotlib.pyplot as plt

frecventa = 100
def sinus(t):
    return np.sin(2*np.pi*frecventa*t)

fv_esnt = 1000
x = np.linspace(0,1,fv_esnt)
y = sinus(x)

i = 0
x1 = []
y1 = []
while(i < fv_esnt):
    x1 += [x[i]]
    y1 += [y[i]]
    i+=4

i = 1
x2 = []
y2 = []
while(i < fv_esnt):
    x2 += [x[i]]
    y2 += [y[i]]
    i+=4

k = 0
plt.stem(x,y)
k += 1
plt.savefig(f'Lab2/grafice/7_{k}.pdf', format="pdf")
plt.show()
plt.stem(x1,y1)
k += 1
plt.savefig(f'Lab2/grafice/7_{k}.pdf', format="pdf")
plt.show()
plt.stem(x2,y2)
k += 1
plt.savefig(f'Lab2/grafice/7_{k}.pdf', format="pdf")
plt.show()
plt.plot(x,y)
k += 1
plt.savefig(f'Lab2/grafice/7_{k}.pdf', format="pdf")
plt.show()
plt.plot(x1,y1)
k += 1
plt.savefig(f'Lab2/grafice/7_{k}.pdf', format="pdf")
plt.show()
plt.plot(x2,y2)
k += 1
plt.savefig(f'Lab2/grafice/7_{k}.pdf', format="pdf")
plt.show()

# pt frecventa = 200, semnalele arata aproximativ la fel, doar cele 2 decimate arata mai rare, iar al doilea arata la fel ca primul decimat, doar ca un pic mai la dreapta
# pt frecventa = 100, semnalele decimate pastreaza doar anumite parti din intreg, ambele pastrand parti diferite