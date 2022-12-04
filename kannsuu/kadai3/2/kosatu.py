from matplotlib import pyplot
import numpy


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


if __name__ == '__main__':
    start, end = 0, 1
    
    x = numpy.linspace(start + 0.000001, end, 10000)
    pyplot.plot(x, numpy.exp(-x) / numpy.sqrt(x), label=r'$\displaystyle\frac{e^{-x}}{\sqrt{x}}$', linestyle='-')
    pyplot.plot(x, 2 * numpy.exp(-x*x), label='$2e^{-t^2}$', linestyle='--')
    pyplot.plot(x, 2 * (numpy.exp(-x)-1) / numpy.sqrt(x), label=r'$\displaystyle\frac{e^{-x}-1}{\sqrt{x}}$', linestyle=':')
    
    pyplot.xlim(0,1)
    pyplot.ylim(-2, 10)
    
    pyplot.xlabel('$x$')
    
    pyplot.tight_layout()
    pyplot.legend()
    pyplot.savefig('kosatu.pdf')
