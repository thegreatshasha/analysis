import numpy as np
import matplotlib.pyplot as plt
from utilities import *
from paircorrelation import pairCorrelationFunction_2D
import numpy as np
import matplotlib.pyplot as plt
import glob

""" Generic plotting stream code. Leave it like this """
plt.ion()
fig = plt.figure(figsize=(5,15))

#plt.xlim( (0, 5) )
#plt.ylim( (0, 5))#1.05 * g_r.max()) )

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

#ax = fig.add_subplot(111)
plt.show()

detection_files = sorted(glob.glob('detections_csv/*'))

size_max = 2000.0
r_max = size_max/4
dr = 10.0

densities = range(10,2000,10)

for data_file in detection_files:
    data = np.loadtxt(data_file, delimiter=',')
    ax1.text(200, 2200, 'density %s'%data_file, style='italic')
    x = data[:,0]
    y = data[:,1]

    g_r, r, reference_indices = pairCorrelationFunction_2D(x, y, size_max, r_max, dr)

    ax1.set_xlim((200,2500))
    ax1.set_ylim((200,2500))

    ax2.set_xlabel('r')
    ax2.set_ylabel('g(r)')


    ax2.set_xlim((0,r_max))
    ax2.set_ylim((0,10))


    #g_r, r, reference_indices = pairCorrelationFunction_2D(x, y, 20.0, 5, 0.1)
    #ax.scatter(x,y)
    ax1.scatter(x,y)
    
    ax2.plot(r, g_r, color='black')
    
    plt.pause(0.5)
    
    ax1.cla()
    ax2.cla()
    #plot_adsorbed_circles(x, y, 0.1, 20, reference_indices=reference_indices)
