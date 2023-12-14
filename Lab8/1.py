import numpy as np
import matplotlib.pyplot as plt

# a

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
plt.savefig("Lab8/grafice/1a.pdf", format="pdf")
plt.savefig("Lab8/grafice/1a.png", format="png")
plt.show()


# b
y = np.correlate(serie,serie,mode="full") / np.linalg.norm(serie)

plt.plot(x,y[N-1:])
plt.savefig("Lab8/grafice/1b.pdf", format="pdf")
plt.savefig("Lab8/grafice/1b.png", format="png")
plt.show()

# c
def predict_AR(y,p,m):
    #ar = y[:m+p]
    ar = []
    for i in range(m+p):
        ar.append(y[i])
    i=m+p
    while i<N:
        yy = y[i-1-m+1:i-1+1]
        YY = np.zeros((m,p))
        for j in range(m):
            for l in range(p):
                YY[j][l] = y[i-2-j-l]
        xx = np.linalg.lstsq(YY,yy,rcond=-1)[0]
        pred = 0
        for j in range(p):
            pred += y[i-1-j]*xx[j]
        ar.append(pred)
        i += 1
    return ar

ar = predict_AR(serie,10,25)
plt.plot(serie,label="y")
plt.plot(ar,label="ar")
plt.legend(loc="upper left")
plt.savefig("Lab8/grafice/1c.pdf", format="pdf")
plt.savefig("Lab8/grafice/1c.png", format="png")
plt.show()

# d
minim = np.mean([(serie[i]-ar[i])**2 for i in range(N)])
bestp=10
bestm=25
for p in range(25):
    for m in range(25):
        ar = predict_AR(serie,p,m)
        eroare = np.mean([(serie[i]-ar[i])**2 for i in range(N)])
        if eroare < minim:
            minim = eroare
            bestp = p
            bestm = m
print(eroare,bestp,bestp)
# 3771.229283528192 24 24