import numpy as np
import matplotlib.pyplot as plt
import scipy
import math
import time
import sounddevice

rate, x = scipy.io.wavfile.read('Lab4/recording.wav')
x = [y[0] for y in x]
N = len(x)
grupuri = []
i=0
pas=0.5

while i+2*pas<=100:
    grupuri += [[x[j] for j in range(int(N*i/100),int(N*(i+2*pas)/100))]]
    i+=pas

a = np.zeros((len(grupuri[0])+1,len(grupuri)))
j=0
for grup in grupuri:
    fft = np.fft.fft(grup)
    for i in range(len(grup)):
        a[i][j]=abs(fft[i])
    j+=1

plt.imshow(a,aspect=0.1, norm = 'log',cmap='plasma')
plt.savefig("Lab4/grafice/6.pdf", format="pdf")
plt.savefig("Lab4/grafice/6.png", format="png")
plt.show()