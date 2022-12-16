from typing import Callable

import numpy
from matplotlib import pyplot


class Function:
    def __call__(self, x:float) -> float:
        return x**3 + 2 * x**2 - 5 * x - 6
    
    def __str__(self) -> str:
        return '$f = x^3 + 2x^2 - 5x - 6$'
    
    def df(self, x:float):
        return 3 * x**2 + 4 * x - 5
    
    
def get_zero_points(algorithm:Callable, f:Function, starts:list) -> list[float]:
    return [algorithm(f, start) for start in starts]


def plot_with_zero_points(f:Function, xlim:tuple[float], ylim:tuple[float], zero_points:list[float], save_path:str, n:float=10**7) -> None:
    x = numpy.linspace(*xlim, n)
    
    pyplot.plot(x, f(x), label=str(f))
    pyplot.scatter([zero_point[-1] for zero_point in zero_points], numpy.zeros(len(zero_points)), zorder=10)
    
    pyplot.xlim(xlim)
    pyplot.ylim(ylim)
    
    pyplot.xlabel('$x$')
    pyplot.ylabel('$f$', rotation=0)

    pyplot.grid()
    pyplot.legend()
    pyplot.savefig(save_path)
    