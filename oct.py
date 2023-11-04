import numpy as np
import matplotlib.pyplot as plt
xrange = np.linspace(0, 1000)
top = xrange * 0
def sin(dgr):
    return(np.sin(np.radians(dgr)))
lay1 = sin(xrange / 100) * 20 - 150
datatop = [xrange, top]
datalay1 = [xrange, lay1]
plt.plot(*datatop, *datalay1)
plt.grid()
plt.show()