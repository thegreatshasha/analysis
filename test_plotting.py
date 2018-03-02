import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig = plt.figure()
plt.show()

data = np.loadtxt('detections_csv/vid15_3500.csv', delimiter=',')
x = data[:,0]
y = data[:,1]

ax1 = fig.add_subplot(212)
ax2 = fig.add_subplot(222)

ax1.scatter(x,y, c='black')
ax2.scatter(x,y, c='green')
plt.pause(0.5)
plt.cla()