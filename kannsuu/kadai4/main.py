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


if __name__ == '__main__':
    ns = [4, 8, 16, 32, 64, 128]
    markers = {
        4: '.',
        8: '.',
        16: '.',
        32: '.',
        64: '.',
        128: '.',
        256: '.',
    }
    
    for n in ns:
        ts, us = readfile(f'{n}.txt')
        pyplot.plot(ts, us, label=f'$n={n}$', marker=markers[n])
        
    x = numpy.linspace(0, 1, 10000)
    pyplot.plot(x, 8 * x * (x * x - 1), label=f'$u=8x(x^2-1)$', linestyle='--')
    
    pyplot.xlim(0, 1)
    
    pyplot.xlabel('$x$')
    pyplot.ylabel('$u$', rotation=0)
    
    #pyplot.xscale('log')
    #pyplot.yscale('log')
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('main.pdf')
