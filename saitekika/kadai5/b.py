import numpy
from matplotlib import pyplot

from function import Function, backtrack, plot_with_critical_point


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def get_critical_point_with_newton(f:Function, start:numpy.array, terminate_threshold:float=10**-7) -> list[numpy.array]:
    x:numpy.array = start
    k = 0
    
    xs:list[tuple[float]] = [x.copy()]
    last_f:float = float('inf')
    while abs(last_f - f(x)) > terminate_threshold:
        d:numpy.array = numpy.array(-f.d2f(x).I @ f.df(x))[0]
        t:float = backtrack(f, x, d, 10**-4, 0.5, 1)
        
        last_f = f(x)
        x += d * t
        
        xs.append(x.copy())
        k += 1
    
    return xs


if __name__ == '__main__':
    f:Function = Function()
    critical_point:list[float] = get_critical_point_with_newton(f, numpy.array([2.0, 0.0]), 10**-8)
    print(critical_point)
    print(f(critical_point[-1]))
    print(len(critical_point))
    # plot_with_critical_point(f, xlim=(-5, 5), critical_point=critical_point, save_path='a.pdf')
