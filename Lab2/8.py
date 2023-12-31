import numpy as np
import matplotlib.pyplot as plt

def Pade(a):
    return (a-7*a**3/60)/(1+a**2/20)

start = -np.pi/2
end = np.pi/2
nr_esantioane = 100

x = np.linspace(start,end,nr_esantioane)
y0 = np.sin(x)
y1 = x
y2 = Pade(x)
y3 = y1 - y0
y4 = y2 - y0

plt.plot(x,y0)
plt.title("sin")
plt.savefig(f'Lab2/grafice/8_sin.pdf', format="pdf")
plt.show()

plt.plot(x,y1)
plt.title("y=x")
plt.savefig(f'Lab2/grafice/8_y=x.pdf', format="pdf")
plt.show()

plt.plot(x,y2)
plt.title("Pade")
plt.savefig(f'Lab2/grafice/8_Pade.pdf', format="pdf")
plt.show()

plt.plot(x,y3)
plt.title("y=x fata de sin")
plt.savefig(f'Lab2/grafice/8_y=x_fata_de_sin.pdf', format="pdf")
plt.show()

plt.plot(x,y4)
plt.title("Pade fata de sin")
plt.savefig(f'Lab2/grafice/8_Pade_fata_de_sin.pdf', format="pdf")
plt.show()
