import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

rc('text', usetex=True)

def g1(h):
    return (np.exp(h) - 1) / h

def g2(h):
    return (np.exp(0.5 * h) - np.exp(-0.5 * h)) / h

def E(g):
    return np.abs(g - 1)

hs = np.logspace(-10, 0, 100)
E1s = []
E2s = []

for h in hs:
    E1s.append(E(g1(h)))
    E2s.append(E(g2(h)))
    
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e-10, 1)
plt.plot(hs, E1s, label='$E_1(h)$')
plt.plot(hs, E2s, label='$E_2(h)$')
plt.xlabel('$h$')
plt.ylabel('$E$', rotation=0)
plt.legend()
plt.savefig('E.eps')