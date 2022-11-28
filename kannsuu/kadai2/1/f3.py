from matplotlib import pyplot
import numpy


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, u = line.split()
        ts.append(float(t))
        us.append(float(u))
        
    return ts, us


def f(x):
    return 1 / (1 + 25 * x**2)


if __name__ == '__main__':
    start, end = -1, 1
    
    markers = {
        16: '.',
        8: 'd',
        4: '^',
        2: 'v'
    }
    for n in [16, 8, 4, 2]:
        ts, us = readfile(f'f3n{n}.txt')
        pyplot.plot(ts, us, label=f'$n = {n}$', marker=markers[n], markevery=len(ts) // n)
        
    x = numpy.linspace(start, end, 10000)
    pyplot.plot(x, f(x), linestyle='--', label=r'$\displaystyle\frac{1}{1+25x^2}$', color='black')
    
    pyplot.xlim(start, end)
    pyplot.ylim(-4, 2)
    
    pyplot.xlabel('$x$')
    pyplot.ylabel('$P$', rotation=0)
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('f3.pdf')
