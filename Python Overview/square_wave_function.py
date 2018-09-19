import numpy as np
import matplotlib.pyplot as plt

#this function is the approximation of a square wave
def square_component(x,omega,k):
    val = (4.0/np.pi)* np.sin(2*np.pi*(2*k-1)*omega*x)/(2*k-1)
    return val

#adds up to the nth term of the sum notation approximation of square wave
def square_approx(x, omega, n):
    val = 0;
    for i in range(1, n+1):
        val = val + square_component(x, omega, i)
    return val

# initial variables
omega=2
x = np.linspace(0,1,500)
y = np.zeros([6, len(x)])
k = [1, 2, 8, 32, 128, 512]

# for every row in y, we fill it with all the y values,
# with each row corresponding to a different value of x
for i in range(len(k)):
    y[i, :] = square_approx(x, omega, k[i])
    plt.plot(y[i])

plt.show()
