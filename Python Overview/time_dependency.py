import numpy as np
import matplotlib.pyplot as plt
import quantumworldX as qw

t = np.arange(0,5+0.01,0.01) # 0.01 is to include the endpoint
x = np.linspace(0,2*np.pi,200)
y = np.zeros((len(x),len(t)))
# for-loop
for indt in range(0,len(t)):
    ti = t[indt]
    y[:,indt] = np.sin(x)*np.sin(ti) #using the formula of a vibrating standing wave
# plot stuff
qw.time_plot(x,y,t,2)
plt.show()
