import numpy as np
import matplotlib.pyplot as plt


# read data from file co2_daily_mlo.csv
file = open('Lab10/co2_daily_mlo.csv', 'r')
data = []
for line in file.readlines()[32:]:
    data += [line.strip().split(',')]
N = len(data)
year = np.zeros(N)
month = np.zeros(N)
day = np.zeros(N)
decimal = np.zeros(N)
co2 = np.zeros(N)
for i in range(N):
    year[i] = int(data[i][0])
    month[i] = int(data[i][1])
    day[i] = int(data[i][2])
    decimal[i] = float(data[i][3])
    co2[i] = float(data[i][4])
# plot data
plt.plot(decimal, co2)
plt.savefig(f"Lab10/grafice/3_a_daily.pdf", format="pdf")
plt.savefig(f"Lab10/grafice/3_a_daily.png", format="png")
plt.show()

# average for every month over all period
NN = year[N-1]*12+month[N-1]-year[0]*12-month[0]+1
NN = int(NN)
monthly_sum = np.zeros(NN, dtype=float)
monthly_count = np.zeros(NN)
monthly_average = np.zeros(NN, dtype=float)
for i in range(N):
    monthly_sum[int((year[i]-year[0])*12+month[i]-month[0])] += co2[i]
    monthly_count[int((year[i]-year[0])*12+month[i]-month[0])] += 1
    
for i in range(len(monthly_average)):
    if monthly_count[i] != 0:
        monthly_average[i] = float(monthly_sum[i]/monthly_count[i])
    else:
        monthly_average[i] = monthly_average[i-1]

# plot data
plt.plot(monthly_average)
plt.savefig(f"Lab10/grafice/3_a_monthly.pdf", format="pdf")
plt.savefig(f"Lab10/grafice/3_a_monthly.png", format="png")
plt.show()

# find trend (liniar model) for monthly_average with lstsw
x = np.arange(NN)
A = np.zeros((NN, 2))
A[:, 0] = x
A[:, 1] = 1
monthly_average = np.array(monthly_average)
m, c = np.linalg.lstsq(A, monthly_average, rcond=None)[0]
linear_trend = m*x+c
plt.plot(linear_trend)
plt.savefig(f"Lab10/grafice/3_b_trend.pdf", format="pdf")
plt.savefig(f"Lab10/grafice/3_b_trend.png", format="png")
plt.show()
# eliminate trend from monthly_average
monthly_average_no_trend = monthly_average-linear_trend

# plot data
plt.plot(monthly_average_no_trend)
plt.savefig(f"Lab10/grafice/3_b_monthly_no_trend.pdf", format="pdf")
plt.savefig(f"Lab10/grafice/3_b_monthly_no_trend.png", format="png")
plt.show()

def ornstein_uhlenbeck(x,y,alpha=7):
    return np.exp(-alpha*np.abs(x-y))

# regression for monthly_average_no_trend
N = len(monthly_average_no_trend)
A = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        A[i, j] = ornstein_uhlenbeck(i, j)
b = monthly_average_no_trend
a = np.linalg.solve(A, b)
# plot data and regression
plt.plot(monthly_average_no_trend[:NN//5*4])
plt.plot(x[NN//5*4:],a[NN//5*4:])
plt.savefig(f"Lab10/grafice/3_c_regression.pdf", format="pdf")
plt.savefig(f"Lab10/grafice/3_c_regression.png", format="png")
plt.show()


