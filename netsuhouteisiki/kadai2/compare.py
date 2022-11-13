from matplotlib import pyplot
import numpy


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, *u = line.split()
        ts.append(float(t))
        us.append(list(map(float, u)))
        
    return ts, us


if __name__ == '__main__':
    ts25, us25 = readfile('25.txt')
    ts50, us50 = readfile('50.txt')
    ts100, us100 = readfile('100.txt')
    
    x = numpy.concatenate([numpy.array([0]), numpy.arange(0.025, 200, 0.05), numpy.array([200])])
    pyplot.plot(x, us25[40000], label='$b = 0.25$', marker='.', markevery=0.05)
    pyplot.plot(x, us50[40000], label='$b = 0.5$', marker='s', markevery=0.05)
    pyplot.plot(x, us100[40000], label='$b = 1$', marker='d', markevery=0.05)
    
    pyplot.xlim(0, 200)
    pyplot.xticks([0, 25, 50, 75, 100, 125, 150, 175, 200])
    
    pyplot.xlabel('$x$')
    pyplot.ylabel('$u$', rotation=0)
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('compare.pdf')
