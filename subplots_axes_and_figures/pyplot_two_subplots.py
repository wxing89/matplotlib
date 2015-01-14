import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# optional because figure(1) will be created by default
plt.figure(1)
# subplt() specifies numrows, numcols, fignum where fignum
# ranges from 1 to numrows*numcols. The commas in the subplot
# command are optional if numrows*numcols<10. So subplot(211)
# is identical to subplot(2,1,1).
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') # 'k' means black

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
