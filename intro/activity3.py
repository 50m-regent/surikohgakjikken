import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.01, 1, 0.001)

plt.xlim(0, 1)
plt.plot(a, 2 * a)
plt.savefig('lin.eps')

plt.cla()

plt.xlim(0, 1)
plt.yscale('log')
plt.plot(a, np.exp(2 * a))
plt.savefig('exp.eps')

plt.cla()

plt.xlim(0.01, 1)
plt.xscale('log')
plt.yscale('log')
plt.plot(a, a * a)
plt.savefig('pow.eps')