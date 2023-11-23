import numpy as np
import matplotlib.pyplot as plt
import math
import time

Ns = [128, 256, 512, 1024, 2048, 4096, 8192]

frecventa = 5
def sinusoida(t):
    return np.sin(2*np.pi*frecventa*t)


normal = []
rapid = []

for N in Ns:

    x = np.linspace(0,1,N)
    y = sinusoida(x)

    start = time.time()
    start = time.perf_counter()
    F = [[0 for i in range(N)] for j in range(N)]
    for a in range(N):
        for b in range(N):
            F[a][b] = math.e**(2*np.pi*1j*a*b/N)
    rez = np.matmul(F,y)
    end = time.time()
    print(end-start)
    normal+=[end-start]

    # start = time.time()
    start = time.perf_counter()
    rez = np.fft.fft(y)
    # end = time.time()
    end = time.perf_counter()
    print(end-start)
    if(end==start):
        end+=0.000001
        print("Inca nu e indeajuns de precis") # nu a ajuns
    rapid+=[end-start]

plt.yscale("log")
plt.plot(Ns,normal,label="dft")
plt.plot(Ns,rapid,label="fft")
plt.legend()
plt.savefig("Lab4/grafice/1.pdf", format="pdf")
plt.savefig("Lab4/grafice/1.png", format="png")
plt.show()
