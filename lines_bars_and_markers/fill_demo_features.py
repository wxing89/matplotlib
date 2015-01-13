"""
Demo of the fill function with a few features.

In addition to the basic fill plot, this demo shows a few optional features:

    * Multiple curves with a single command.
    * Setting the fill color.
    * Setting the opacity (alpha value).
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(start=0, stop=2 * np.pi, num=100)
y1 = np.sin(x)
y2 = np.sin(3 * x)

# alpha: float (0.0 transparent through 1.0 opaque)
plt.fill(x, y1, 'b', x, y2, 'r', alpha=0.5)
plt.show()
