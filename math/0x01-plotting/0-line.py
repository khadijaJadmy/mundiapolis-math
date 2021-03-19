#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, 'r')

plt.xticks(np.arange(0, 12, 2))
plt.yticks(np.arange(0, 1200, 200))
plt.xlim([0, 10])
plt.show()
