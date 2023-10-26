import numpy as np
import matplotlib.pyplot as plt
import math

N = 8
F = [[0 for i in range(N)] for j in range(N)]

for a in range(N):
    for b in range(N):
        F[a][b] = math.e**(2*np.pi*1j*a*b/N)

fig, axs = plt.subplots(N)
fig.suptitle("Partea Reala si Partea Imaginara pentru fiecare linie") 
fig.tight_layout(pad=10.0)

for ax in axs.flat:
    ax.set_xlabel("real")
    ax.set_ylabel("imag")

for a in range(N):
    real = [[F[a][b].real] for b in range(N)]
    imaginar = [[F[a][b].imag] for b in range(N)]
    axs[a].plot(real,imaginar)
    axs[a].set_title(f'Linia {a}')

plt.savefig("Lab3/grafice/1.pdf", format="pdf")
#plt.subplot_tool()
plt.show()

if (1/N * np.matmul(F, np.transpose(F)) == np.identity(N)).all():
    print("Matricea Fourier e unitara")
else:
    print("Matricea Fourier nu e unitara")
    
print(np.matmul(F, np.transpose(F)))

