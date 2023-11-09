import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('Lab5/Train.csv', delimiter=',')
x = x[1:]

### a)
# Frecventa de esantionare este de 1 data pe ora <=> 1/3600 ori per secunda <=> 1/3600 Hz <=> 0.0002777777 Hz

### b)
# Esantioanele din fisier acopera intervalul de timp de la 25-08-2012 00:00 la 25-09-2014 23:00

### c)
# Frecventa maxima prezenta in semnal ar fi 0.0002777777 /2 = 0.0001388885

fvmax = max(x[:,2])
print(fvmax)

### d)
