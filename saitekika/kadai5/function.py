import numpy
from matplotlib import pyplot


class Function:
    y:list[float] = [1.5, 2.25, 2.625]
    
    def f(self, i:int, x:numpy.array) -> float:
        assert 2 == len(x)
        return self.y[i] - x[0] * (1 - x[1] ** (i + 1))
    
    def dfi(self, i:int, x:tuple[float]) -> numpy.array:
        assert 2 == len(x)
        return numpy.array([
            -1 + x[1] ** (i + 1),
            (i + 1) * x[0] * (x[1] ** i)
        ])
        
    def dfi2(self, i:int, x:tuple[float]) -> numpy.matrix:
        assert 2 == len(x)
        return numpy.matrix([
            [self.dfi(i, x)[0] * self.dfi(i, x)[0], self.dfi(i, x)[0] * self.dfi(i, x)[1]],
            [self.dfi(i, x)[1] * self.dfi(i, x)[0], self.dfi(i, x)[1] * self.dfi(i, x)[1]]
        ])
    
    def d2fi(self, i:int, x:tuple[float]) -> numpy.matrix:
        assert 2 == len(x)
        return numpy.matrix([
            [0, (i + 1) * (x[1] ** i)],
            [(i + 1) * (x[1] ** i), 0 if 0 == i else i * (i + 1) * x[0] * (x[1] ** (i - 1))]
        ])
    
    def __call__(self, x:tuple[float]) -> float:
        return sum(self.f(i, x)**2 for i in range(3))
    
    def df(self, x:numpy.array) -> numpy.array:
        return 2 * sum(self.f(i, x) * self.dfi(i, x) for i in range(3))
    
    def d2f(self, x:numpy.array) -> numpy.matrix:
        return 2 * sum(self.f(i, x) * self.d2fi(i, x) + self.dfi2(i, x) for i in range(3))
        
        
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
    