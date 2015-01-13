"""
Simple demo of the fill function.
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(start=0, stop=1, num=100)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

plt.fill(x, y, 'lime')
plt.grid(True)
plt.show()
