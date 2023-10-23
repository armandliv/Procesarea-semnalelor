import numpy as np
import matplotlib.pyplot as plt

def sinus(t,frecventa):
    return np.sin(2*np.pi*frecventa*t)

fs = 20



# graficul da eroare pt fs/2 si fs
#
# pas = 1/200
# def genereaza(frecventa):
#     t = 0
#     xx = []
#     yy = []
#     while t <= 0.2:
#         xx += [t]
#         yy += [sinus(t,frecventa)]
#         t+=pas
#     plt.plot(xx,yy)
#     plt.show()

xx = np.linspace(0,1,fs)

k = 0
def genereaza(frecventa):
    yy = sinus(xx,frecventa)
    plt.plot(xx,yy)
    global k
    k += 1
    plt.savefig(f'Lab2/grafice/6_{k}.pdf', format="pdf")
    plt.show()

#genereaza(fs)
genereaza(fs/2)
genereaza(fs/4)
genereaza(0)

# fluctuatiile sunt din ce in ce mai rare
# fs/2 alterneaza valori pzotitive cu negative, iar la fs/4 fiecare spike de la fs/2 a fost esantionat in 2 puncte