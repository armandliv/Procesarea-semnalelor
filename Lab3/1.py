import numpy as np
import matplotlib.pyplot as plt
import math

N = 8
F = [[0 for i in range(N)] for j in range(N)]

for a in range(N):
    for b in range(N):
        F[a][b] = math.e**(2*np.pi*1j*a*b/N)

fig, axs = plt.subplots(N,figsize=(10,10))
fig.suptitle("Partea Reala si Partea Imaginara pentru fiecare linie") 
fig.tight_layout(pad=2)


for a in range(N):
    index = [b for b in range(N)]
    real = [[F[a][b].real] for b in range(N)]
    imaginar = [[F[a][b].imag] for b in range(N)]
    axs[a].plot(index,real,label="Real")
    axs[a].plot(index,imaginar,label="Imaginar")
    axs[a].set_title(f'Linia {a}')

plt.legend(loc="lower right")
plt.savefig("Lab3/grafice/1.pdf", format="pdf")
plt.savefig("Lab3/grafice/1.png", format="png")
#plt.subplot_tool()
plt.show()

M1 = 1/N * np.matmul(F, np.conj(np.transpose(F)))  
M2 = np.identity(N)
ok = 1
eps = 0.0000001

for i in range(N):
    for j in range(N):
        if abs(M1[i][j]-M2[i][j])>eps:
            ok = 0

if ok == 1:
    print("Matricea Fourier e unitara")
else:
    print("Matricea Fourier nu e unitara")
# e unitara

