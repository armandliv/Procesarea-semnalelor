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

max = max(x)/len(x)/3600
print(max)

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
# da, componenta continua este 0
print(X[0])
print(sum(x)/N)
xx = [y-X[0] for y in x]

X = np.fft.fft(xx)
X = abs(X/N)
X = X[:N//2]
fs = 1/3600
f = fs*np.linspace(0,N/2,N//2)/N;
plt.plot(f,X)
plt.savefig("Lab5/grafice/e.pdf", format="pdf")
plt.savefig("Lab5/grafice/e.png", format="png")
plt.show()

### f)
X = np.fft.fft(x)
X = abs(X/N)
X = X[:N//2]


indici = np.argsort(X)[-6:][::-1]
for index in indici:
    print(f[index],"Hz", 1/(f[index]*(1/fs)*24), "zile")

# 0.0 Hz inf zile
# 1.5190734866989925e-08 Hz 761.9166666666667 zile
# 3.038146973397985e-08 Hz 380.95833333333337 zile
# 1.1575339968646325e-05 Hz 0.9998906386701661 zile
# 4.557220460096978e-08 Hz 253.97222222222217 zile
# 1.6557901005019021e-06 Hz 6.990061162079511 zile

### g
st = 2400 # 3 dec 2012 (luni)
dr = 2400 + 24*31
xs = np.linspace(0,31,24*31)
ys = []
for i in range(st,dr):
    ys+=[x[i]]
plt.plot(xs,ys)
plt.savefig("Lab5/grafice/g.pdf", format="pdf")
plt.savefig("Lab5/grafice/g.png", format="png")
plt.show()
# se vede peakul in weekendul de dinainte de craciun HAHA XD
# (nu weekendul 22-23, ci cel de dinainte)

### h)
# Intai putem incerca sa determinam cate esantioane fac un an
# Pentru acest lucru putem urmari date calendaristice despre care stim ca sunt mai aglomerate: Craciun(cum am observat mai sus), Paste, Anul Nou, inceperea scolii si orice alta perioada despre care am avea date adunate care ar evidentia perioadele mai speciale
# Dupa ce reusim sa matchuirea dintre acestea si esantioanlee semnalului, calculul date de inceput devine usor
# Un neajuns ar fi ca aceasta metoda nu merge pt perioade mai scurte de un an, iar altul ar fi ca trebuie sa ne asiguram(prin alte masuratori) ca presupunerile noastre de date mai speciale sunt corecte 

### i)
# Vreau ca flimita sa fie 1 data la 3 ore

flimita = fs/3
X = np.fft.fft(x)
f = fs*np.linspace(0,N,N)/N;

for i in range(len(X)):
    if f[i] > flimita:
        X[i] = 0

xx = np.fft.ifft(X)

plt.plot(f,X)
plt.savefig("Lab5/grafice/i1.pdf", format="pdf")
plt.savefig("Lab5/grafice/i1.png", format="png")
plt.show()

plt.plot(xx.real)
plt.savefig("Lab5/grafice/i2.pdf", format="pdf")
plt.savefig("Lab5/grafice/i2.png", format="png")
plt.show()

plt.plot(x)
plt.savefig("Lab5/grafice/i3.pdf", format="pdf")
plt.savefig("Lab5/grafice/i3.png", format="png")
plt.show()

plt.plot(xx.real[st:dr])
plt.savefig("Lab5/grafice/i4.pdf", format="pdf")
plt.savefig("Lab5/grafice/i4.png", format="png")
plt.show()

plt.plot(x[st:dr])
plt.savefig("Lab5/grafice/i5.pdf", format="pdf")
plt.savefig("Lab5/grafice/i5.png", format="png")
plt.show()