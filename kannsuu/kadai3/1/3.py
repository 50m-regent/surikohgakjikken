from matplotlib import pyplot
import numpy


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 18


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
    start, end = 0, 10
    
    markers = {
        4: '.',
        5: 'd',
        6: '^',
        7: 'v'
    }
    real = {
        4: numpy.log(2),
        5: (numpy.exp(5) - numpy.exp(-5)) / 5,
        6: 2 + numpy.pi,
        7: 2 * numpy.pi
    }
    for i in [4, 5, 6, 7]:
        ts, us = readfile(f'f{i}-3.txt')
        pyplot.plot(ts, [numpy.abs(u - real[i]) ** 1.5 if numpy.abs(u - real[i]) **1.5 > 10**-5 else 10**-5 for u in us], label=f'$E_n(f_{i})$', marker=markers[i])
    
    n = numpy.logspace(0, 3, 10000)
    pyplot.plot(n, 100 * n ** -1.5, label='$\Theta(n^{-1.5})$', linestyle='--', color='black')
    
    pyplot.xlim(2**start, 2**end)
    # pyplot.ylim(10**-8,10**8)
    
    pyplot.xlabel('$n$')
    pyplot.ylabel('$E$', rotation=0)
    
    pyplot.xscale('log')
    pyplot.yscale('log')
    
    pyplot.tight_layout()
    pyplot.legend(loc='upper right')
    pyplot.savefig('3.pdf')
