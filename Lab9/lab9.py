import numpy as np
import matplotlib.pyplot as plt

# 1
N = 1000

x = np.linspace(0,1,N)

def ecuatie2(t):
    return 8*t*t+2*t+1

def sinusoida(t,frecventa):
    return np.sin(2*np.pi*frecventa*t)

trend = ecuatie2(x)
sezon = sinusoida(x,5) + sinusoida(x,7)
variatii = np.random.normal(0,1,N)
serie = trend + sezon + variatii

fig, axs = plt.subplots(4)
fig.tight_layout(pad=1)

axs[0].plot(serie)
axs[0].set_title("Serie")
axs[1].plot(trend)
axs[1].set_title("Trend")
axs[2].plot(sezon)
axs[2].set_title("Sezon")
axs[3].plot(variatii)
axs[3].set_title("Variatii")
plt.savefig("Lab9/grafice/1.pdf", format="pdf")
plt.savefig("Lab9/grafice/1.png", format="png")
plt.show()

# 2
alpha = 0.5
s = np.zeros(N)
s[0] = serie[0]
for i in range(1,N):
    s[i] = alpha*serie[i] + (1-alpha)*s[i-1]

plt.plot(s)
plt.title(f"Alpha fixat = {alpha}")
plt.savefig("Lab9/grafice/2_fixat.pdf", format="pdf")
plt.savefig("Lab9/grafice/2_fixat.png", format="png")
plt.show()

suma_min = 0
for i in range(N-1):
    suma_min += (s[i] - serie[i+1])*(s[i] - serie[i+1])
alpha_min = alpha

alpha = 0
while alpha <= 1:
    s = np.zeros(N)
    s[0] = serie[0]
    for i in range(1,N):
        s[i] = alpha*serie[i] + (1-alpha)*s[i-1]
    suma = 0
    for i in range(N-1):
        suma += (s[i] - serie[i+1])*(s[i] - serie[i+1])
    if(suma < suma_min):
        suma_min = suma
        alpha_min = alpha
    alpha += 0.01

print("Alpha optim: ", alpha_min)
s = np.zeros(N)
s[0] = serie[0]
for i in range(1,N):
    s[i] = alpha_min*serie[i] + (1-alpha_min)*s[i-1]

plt.plot(s)
plt.title(f"Alpha optim = {alpha_min}")
plt.savefig("Lab9/grafice/2_optim.pdf", format="pdf")
plt.savefig("Lab9/grafice/2_optim.png", format="png")
plt.show()



