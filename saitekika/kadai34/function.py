import numpy
from matplotlib import pyplot


class Function:
    def __call__(self, x:tuple[float]) -> float:
        assert 2 == len(x)
        return x[0]**2 + numpy.exp(x[0]) + x[1]**4 + x[1]**2 - 2 * x[0] * x[1] + 3
    
    def df(self, x:tuple[float]) -> numpy.array:
        assert 2 == len(x)
        return numpy.array([
            2 * x[0] + numpy.exp(x[0]) - 2 * x[1],
            4 * x[1]**3 + 2 * x[1] - 2 * x[0]
        ])
    
    def d2f(self, x:tuple[float]) -> numpy.matrix:
        assert 2 == len(x)
        return numpy.matrix([
            [2 + numpy.exp(x[0]), -2],
            [-2, 12 * x[1]**2 + 2]
        ])
        
        
def backtrack(
    f:Function,
    x:numpy.array,
    d:numpy.array,
    zeta:float,
    rho:float,
    t:float
) -> float:
    while f(x + t * d) > f(x) + zeta * t * numpy.dot(d, f.df(x)):
        t *= rho
        
    return t


def plot_with_critical_point(f:Function, xlim:tuple[float], critical_point:float, save_path:str, n:float=10**7) -> None:
    x = numpy.linspace(*xlim, n)
    
    pyplot.plot(x, f(x), label=str(f))
    pyplot.scatter(critical_point[-1], f(critical_point[-1]), zorder=10)
    
    pyplot.xlim(xlim)

    pyplot.grid()
    pyplot.legend()
    pyplot.savefig(save_path)
    