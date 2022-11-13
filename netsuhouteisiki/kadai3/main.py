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
    ts, us = readfile('main.txt')
    
    x = numpy.concatenate([numpy.array([-10]), numpy.arange(-9.975, 10, 0.05), numpy.array([10])])
    pyplot.plot(x, us[999], label='$t = 1$', marker='.', markevery=0.05)
    pyplot.plot(x, us[1999], label='$t = 2$', marker='s', markevery=0.05)
    pyplot.plot(x, us[2999], label='$t = 3$', marker='d', markevery=0.05)
    pyplot.plot(x, us[3999], label='$t = 4$', marker='v', markevery=0.05)
    pyplot.plot(x, us[4999], label='$t = 5$', marker='<', markevery=0.05)
    pyplot.plot(x, us[5999], label='$t = 6$', marker='>', markevery=0.05)
    pyplot.plot(x, us[6999], label='$t = 7$', marker='^', markevery=0.05)
    pyplot.plot(x, us[7999], label='$t = 8$', marker='p', markevery=0.05)
    
    pyplot.xlim(-10, 10)
    pyplot.xticks([-10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10])
    
    pyplot.xlabel('$x_j$')
    pyplot.ylabel('$(R^n_j)^2 + I^n_jI^{n-1}_j$')
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('main.pdf')
