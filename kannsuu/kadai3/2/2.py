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
        1: '.',
        2: 'd',
        3: '^',
    }
    real = 1.49364826562
    for i in [1, 2, 3]:
        ts, us = readfile(f'{i}-2.txt')
        pyplot.plot(ts, [numpy.abs(u - real) for u in us], label=f'Method {i}', marker=markers[i])
        
    n = numpy.logspace(0, 3, 10000)
    pyplot.plot(n, n ** -0.5, label='$\Theta(n^{-0.5})$', linestyle=':', color='black')
    pyplot.plot(n, n ** -1, label='$\Theta(n^{-1})$', linestyle='--', color='black')
    
    pyplot.xlim(2**start, 2**end)
    
    pyplot.xlabel('$n$')
    pyplot.ylabel('$E$', rotation=0)
    
    pyplot.xscale('log')
    pyplot.yscale('log')
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('2.pdf')
