import numpy
from matplotlib import pyplot

from function import Function


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def plot(f:Function, xlim:tuple[int], ylim:tuple[int], save_path:str, n=10**7) -> None:
    x = numpy.linspace(*xlim, n)
    pyplot.plot(x, f(x), label=str(f))
    
    pyplot.xlim(xlim)
    pyplot.ylim(ylim)
    
    pyplot.xlabel('$x$')
    pyplot.ylabel('$f$', rotation=0)
    
    pyplot.grid()
    pyplot.legend()
    pyplot.savefig(save_path)


if __name__ == '__main__':
    f = Function()
    plot(f, xlim=(-10, 10), ylim=(-10, 10), save_path='a.pdf')
