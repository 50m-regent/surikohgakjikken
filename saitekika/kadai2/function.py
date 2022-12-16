import numpy
from matplotlib import pyplot


class Function:
    def __call__(self, x:float) -> float:
        return x**3 / 3 - x**2 - 3 * x + 5 / 3
    
    def __str__(self) -> str:
        return r'$f=\displaystyle\frac{1}{3}x^3 - x^2 - 3x + \frac{5}{3}$'
    
    def df(self, x:float):
        return x**2 - 2 * x - 3
    
    def d2f(self, x:float):
        return 2 * x - 2


def plot_with_critical_point(f:Function, xlim:tuple[float], critical_point:float, save_path:str, n:float=10**7) -> None:
    x = numpy.linspace(*xlim, n)
    
    pyplot.plot(x, f(x), label=str(f))
    pyplot.scatter(critical_point[-1], f(critical_point[-1]), zorder=10)
    
    pyplot.xlim(xlim)
    
    pyplot.xlabel('$x$')
    pyplot.ylabel('$f$', rotation=0)

    pyplot.grid()
    pyplot.legend()
    pyplot.savefig(save_path)
    