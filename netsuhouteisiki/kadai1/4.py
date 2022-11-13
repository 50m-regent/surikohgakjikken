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
    ts, us = readfile('4.txt')
    
    x = numpy.concatenate([numpy.array([0]), numpy.arange(0.025, 10, 0.05), numpy.array([10])])
    pyplot.plot(x, us[100], label='$u(x, 1)$', marker='.', markevery=10)
    pyplot.plot(x, us[200], label='$u(x, 2)$', marker='s', markevery=10)
    pyplot.plot(x, us[300], label='$u(x, 3)$', marker='d', markevery=10)
    pyplot.plot(x, us[400], label='$u(x, 4)$', marker='v', markevery=10)
    pyplot.plot(x, us[500], label='$u(x, 5)$', marker='^', markevery=10)
    
    pyplot.xlim(0, 10)
    pyplot.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    pyplot.xlabel('$x$')
    pyplot.ylabel('$u$', rotation=0)
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('4.pdf')
