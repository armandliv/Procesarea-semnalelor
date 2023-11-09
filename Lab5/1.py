import numpy as np
import matplotlib.pyplot as plt

file = open('Lab5/Train.csv', 'r')
data = []
for line in file.readlines()[1:]:
    data += [line.strip().split(',')]
x = [int(y[2]) for y in data]
N = len(x)


### a)
# Frecventa de esantionare este de 1 data pe ora <=> 1/3600 ori per secunda <=> 1/3600 Hz <=> 0.0002777777 Hz

### b)
# Esantioanele din fisier acopera intervalul de timp de la 25-08-2012 00:00 la 25-09-2014 23:00

### c)
# Frecventa maxima prezenta in semnal ar fi 0.0002777777 /2 = 0.0001388885

fvmax = max(x)/len(x)/3600
print(fvmax)

### d)
X = np.fft.fft(x)
X = abs(X/N)
X = X[:N//2]
fs = 1/3600
f = fs*np.linspace(0,N/2,N//2)/N;
plt.plot(f,X)
plt.savefig("Lab5/grafice/d.pdf", format="pdf")
plt.savefig("Lab5/grafice/d.png", format="png")
plt.show()


### e)
