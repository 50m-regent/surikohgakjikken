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
    start, end = 0, 10
    
    markers = {
        'Midpoint': '.',
        'Trapezoid': 'd',
        'Simpson': 'v'
    }
    for algorithm in ['Midpoint', 'Trapezoid', 'Simpson']:
        ts, us = readfile(f'f7{algorithm}.txt')
        pyplot.plot(ts, [abs(u - 2 * numpy.pi) for u in us], label=f'{algorithm}', marker=markers[algorithm])
        
    n = numpy.logspace(0, 3, 10000)
    pyplot.plot(n, 1.8 * n ** -1, label='$\Theta(n^{-1})$', linestyle='--', color='black')
    
    pyplot.xlim(2**start, 2**end)
    
    pyplot.xlabel('$n$')
    pyplot.ylabel('$E$', rotation=0)
    
    # pyplot.ylim([0.1, 10])
    
    pyplot.xscale('log')
    pyplot.yscale('log')
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('f7.pdf')
