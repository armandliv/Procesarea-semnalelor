import numpy as np
import matplotlib.pyplot as plt
import scipy
### a
file = open('Lab5/Train.csv', 'r')
data = []
for line in file.readlines()[1:]:
    data += [line.strip().split(',')]
x = [int(y[2]) for y in data]
N = len(x)


st = 2400 # 3 dec 2012 (luni)
dr = 2400 + 24*3
xs = np.linspace(0,3,24*3)
ys = []
for i in range(st,dr):
    ys+=[x[i]]

### b
fig, axs = plt.subplots(4)
fig.tight_layout(pad=2)
k=0
for w in [5,9,13,17]:
    y2 = np.convolve(ys, np.ones(w), 'valid') / w
    axs[k].plot(y2);
    axs[k].set_title(f'w={w}')
    k += 1
plt.savefig("Lab6/grafice/4b.pdf", format="pdf")
plt.savefig("Lab6/grafice/4b.png", format="png")
plt.show()


### c
# Frecventa este de 1/3600 Hz
# Frecventa Nyquist este 1/3600/2 = 1/7200 Hz
# Frecventa de taiere -> 1 data la 3 ore = 1/3600/3 = 1/10800
# Valoarea frecventei normalizate e 2/3

### d
b1,a1 = scipy.signal.butter(5, 2/3, btype='low')
b2,a2 = scipy.signal.cheby1(5, 5, 2/3, btype='low')
                            
w,h = scipy.signal.freqz(b1,a1)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title("Butterworth")
plt.savefig("Lab6/grafice/4d_butter.pdf", format="pdf")
plt.savefig("Lab6/grafice/4d_butter.png", format="png")
plt.show()

w,h = scipy.signal.freqz(b2,a2)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title("Chebyshev")
plt.savefig("Lab6/grafice/4d_cheby.pdf", format="pdf")
plt.savefig("Lab6/grafice/4d_cheby.png", format="png")
plt.show()

### e
y_butter = scipy.signal.filtfilt(b1, a1, ys)
y_cheby = scipy.signal.filtfilt(b2, a2, ys)

fig, axs = plt.subplots(3)
fig.tight_layout(pad=2)
axs[0].plot(ys)
axs[0].set_title('Datele brute')
axs[1].plot(y_butter)
axs[1].set_title('Butterworth')
axs[2].plot(y_cheby)
axs[2].set_title('Chebyshev')

plt.savefig("Lab6/grafice/4e.pdf", format="pdf")
plt.savefig("Lab6/grafice/4e.png", format="png")
plt.show()

# Aleg Butterworth, pt ca Chebyshev are diferente mai mari fata de datele brute decat Butterworth

### f

# Butterworth
fig, axs = plt.subplots(4)
fig.tight_layout(pad=1)
k = 0
for ordin in [1,3,5,8]:
    b1,a1 = scipy.signal.butter(ordin, 2/3, btype='low')
    y_butter = scipy.signal.filtfilt(b1, a1, ys)
    axs[k].plot(y_butter);
    axs[k].set_title(f'ordin={ordin}')
    k += 1
plt.savefig("Lab6/grafice/4f_butter.pdf", format="pdf")
plt.savefig("Lab6/grafice/4f_butter.png", format="png")
plt.show()


# Cheby
fig, axs = plt.subplots(5)
fig.tight_layout(pad=1)
k = 0
for (ordin,rp) in [(1,1),(3,9),(5,5),(8,2),(11,11)]:
    b2,a2 = scipy.signal.cheby1(ordin, rp, 2/3, btype='low')
    y_cheby = scipy.signal.filtfilt(b2, a2, ys)
    axs[k].plot(y_cheby);
    axs[k].set_title(f'ordin={ordin} rp={rp}')
    k += 1
plt.savefig("Lab6/grafice/4f_cheby.pdf", format="pdf")
plt.savefig("Lab6/grafice/4f_cheby.png", format="png")
plt.show()


