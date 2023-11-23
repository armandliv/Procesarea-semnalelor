import numpy as np
import matplotlib.pyplot as plt

N = 100
p = np.random.randint(0,100,N)
q = np.random.randint(0,100,N)

r = np.zeros(2*N-1)
for i in range(N):
    for j in range(N):
        r[i+j] += p[i]*q[i]

pfft = np.fft.fft(p)
qfft = np.fft.fft(p)
rfft = pfft*qfft
r2 = np.fft.ifft(rfft)

for i in range(2*N-1):
    print(r[i],r2[i])
