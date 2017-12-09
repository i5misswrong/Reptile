import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10000,10000,1)
y1=8500-0.85*x
y2=7938-0.71*(x-1358)

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
