import numpy as np
import matplotlib.pyplot as plt


n=100

x = np.random.rand(n)

fig, axs = plt.subplots(4)

axs[0].plot(x)
x = np.convolve(x,x)
axs[1].plot(x)
x = np.convolve(x,x)
axs[2].plot(x)
x = np.convolve(x,x)
axs[3].plot(x)

plt.savefig("Lab6/grafice/1.pdf", format="pdf")
plt.savefig("Lab6/grafice/1.png", format="png")
plt.show()
