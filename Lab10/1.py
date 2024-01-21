import numpy as np
import matplotlib.pyplot as plt

def gaussian_distribution(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

N = 1000
x = np.linspace(-10,10,N)
y = gaussian_distribution(x, 0, 1)
plt.plot(x, y)
#plt.show()

x = np.random.normal(0, 1, N)
y = gaussian_distribution(x, 0, 1)
plt.hist(x, bins=200, range=(-10, 10), density=True, color='red', alpha=0.5)
plt.savefig("Lab10/grafice/1_1d.pdf", format="pdf")
plt.savefig("Lab10/grafice/1_1d.png", format="png")
plt.show()

# plt contur pt 2d

def gaussian_distribution_2d(x, mu, sigma): # mu = mean and sigma = covariance matrix
    d = 2 # nr de dimensiuni, il putem prelua din mu sau sigma
    return 1 / ((2 * np.pi) ** (d/2) * np.sqrt(np.linalg.det(sigma))) * np.exp(-0.5 * np.dot(np.dot((x - mu).T, np.linalg.inv(sigma)), (x - mu)))
import numpy as np
import matplotlib.pyplot as plt
zero = np.array([0, 0])
I2 = np.array([[1, 0], [0, 1]])
N = 1000
n = np.random.multivariate_normal(zero, I2, N)

mu = np.array([0, 0])
sigma = np.array([[1, 3/5], [3/5, 2]])
l, u = np.linalg.eig(sigma)
A = np.sqrt(l)
x = np.array([np.dot(np.dot(u,A),n[i]) + mu for i in range(N)])
y = np.array([gaussian_distribution_2d(x[i], mu, sigma) for i in range(N)])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.scatter(n[:,0], n[:,1], y, c='red', marker='o')    
plt.savefig("Lab10/grafice/1_2d.pdf", format="pdf")
plt.savefig("Lab10/grafice/1_2d.png", format="png")
plt.show()
