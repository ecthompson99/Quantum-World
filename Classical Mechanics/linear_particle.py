#importing modules
import numpy as np
import matplotlib.pyplot as plt
import quantumworldX as qw

#initializing variables
v = 1.0 #assume constant velocity, for simplicity
dt = 0.001
m = 1
t = np.arange(0,1+dt,dt) #since arange only goes up to 1-dt
x = np.zeros(1001);

for i in range(1, len(t)):
    x[i] = x[i-1] + dt*v #Uses Euler's Algorithm: new position = old position + change in position * time it took between events
    print(x[i])

qw.time_plot1D(x, t, t_step = 30)

plt.show()
