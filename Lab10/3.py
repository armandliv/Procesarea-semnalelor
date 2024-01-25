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
monthly_sum = np.zeros(NN)
monthly_count = np.zeros(NN)
monthly_average = np.zeros(NN)
for i in range(N):
    monthly_sum[int((year[i]-year[0])*12+month[i]-month[0])] += co2[i]
    monthly_count[int((year[i]-year[0])*12+month[i]-month[0])] += 1
for i in range(len(monthly_average)):
    monthly_average[i] = monthly_sum[i]/monthly_count[i]

# plot data
plt.plot(monthly_average)
plt.savefig(f"Lab10/grafice/3_a_monthly.pdf", format="pdf")
plt.savefig(f"Lab10/grafice/3_a_monthly.png", format="png")
plt.show()










