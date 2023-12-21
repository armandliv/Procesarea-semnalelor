import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

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

# 3

q = 10
m = 10
e = np.random.normal(0,1,N+m)
u = np.mean(serie)
YY = np.zeros((N-q,q))
for i in range(q,N):
    for j in range(q):
        YY[i-q][j] = serie[i-1-j]
th = np.linalg.lstsq(YY,serie[q:]-u-e[q:N],rcond=-1)[0]
print(th)
# [ 0.02343778  0.02354881  0.06249258 -0.01704686  0.12866166  0.01004797 0.08628645 -0.05286671  0.01898387  0.01270362]
yy = serie
for i in range(N,N+m):
    yy = np.append(yy,u+e[i])
    for j in range(q):
        yy[i] += th[j]*e[i-1-j]
plt.plot(yy[:N],color="blue",label="serie")
plt.plot([i for i in range(N,N+m)],yy[N:],color="red",label="predictie")
plt.savefig("Lab9/grafice/3.pdf", format="pdf")
plt.savefig("Lab9/grafice/3.png", format="png")
plt.show()

# 4
NN = 900
model = ARIMA(serie[:NN], order=(1,0,1))
model_fit = model.fit()
predictions = model_fit.predict()
eroare = sum([(serie[i]-predictions[i])*(serie[i]-predictions[i]) for i in range(NN)])
minim = eroare
p_min = 1
q_min = 1
for p in range(1,21):
    for q in range(1,21):
        d = 0
        model = ARIMA(serie[:NN], order=(p,d,q))
        model_fit = model.fit()
        predictions = model_fit.predict()
        eroare = sum([(serie[i]-predictions[i])*(serie[i]-predictions[i]) for i in range(NN)])
        if eroare < minim:
            minim = eroare
            p_min = p
            q_min = q

print(p_min,q_min)
model = ARIMA(serie, order=(p_min,d,q_min))
model_fit = model.fit()
predictions = model_fit.predict()
plt.plot(serie,color="blue",label="serie")
plt.plot(predictions[:NN],color="red",label="predictie")
future_predictions = model_fit.forecast(N-NN)
plt.plot([i for i in range(NN,N)],future_predictions,color="green",label="predictie viitoare")
plt.legend()
plt.savefig("Lab9/grafice/4.pdf", format="pdf")
plt.savefig("Lab9/grafice/4.png", format="png")
plt.show()
