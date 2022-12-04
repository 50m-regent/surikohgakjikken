from matplotlib import pyplot
import numpy


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12

def real_u(x):
    return 8 * x * (x*x-1)


def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, u = line.split()
        ts.append(float(t))
        us.append(float(u))
        
    return ts, us


if __name__ == '__main__':
    ns = [4, 8, 16, 32, 64, 128, 256, 512]
    
    diff = []
    for n in ns:
        ts, us = readfile(f'{n}.txt')
        diff.append(numpy.mean([abs(u - real_u(t)) for t, u in zip(ts, us)]))
    
    pyplot.plot(ns, diff, marker='.', label='$E(n)$')
    
    n1 = numpy.logspace(0, 2, 1000)
    n2 = numpy.logspace(1, 3, 1000)
    pyplot.plot(n1, 2 * n1 ** -2, label='$\Theta(n^{-2})$', linestyle='--')
    pyplot.plot(n2, 0.00005 * n2 ** 1.2, label='$\Theta(n^{1.2})$', linestyle=':')
    
    pyplot.xlim(4, 512)
    pyplot.ylim(2*10**-3, 1)
    
    pyplot.xlabel('$n$')
    pyplot.ylabel('$E$', rotation=0)
    
    pyplot.xscale('log')
    pyplot.yscale('log')
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('diff.pdf')
