import numpy as np
import matplotlib.pyplot as plt

def liniar(x,y):
    return x*y

def miscare_browniana(x,y):
    return min(x,y)

def exponentiala_patrata(x,y,alpha=12):
    return np.exp(-alpha*np.linalg.norm(x-y)**2)

def ornstein_uhlenbeck(x,y,alpha=7):
    return np.exp(-alpha*np.abs(x-y))

def periodic(x,y,alpha=2,beta=3):
    return np.exp(-alpha*np.sin(beta*np.pi*(x-y))**2)

def simetric(x,y,alpha=5):
    return np.exp(-alpha*min(np.abs(x-y),np.abs(x+y))**2)

N = 200
interval = np.linspace(-1,1,N)

def calc(functie):
    covarianta = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            covarianta[i,j] = functie(interval[i],interval[j])
    return covarianta

def rez(functie):
    covarianta = calc(functie)
    z = np.random.multivariate_normal(np.zeros(N),covarianta)
    plt.plot(interval,z)
    plt.title(functie.__name__)
    plt.savefig(f"Lab10/grafice/2_{functie.__name__}.pdf", format="pdf")
    plt.savefig(f"Lab10/grafice/2_{functie.__name__}.png", format="png")
    plt.show()

rez(liniar)
rez(miscare_browniana)
rez(exponentiala_patrata)
rez(ornstein_uhlenbeck)
rez(periodic)
rez(simetric)