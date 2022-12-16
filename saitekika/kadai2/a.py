from matplotlib import pyplot

from function import Function, plot_with_critical_point


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def get_critical_point_with_gradient(f:Function, start:float, terminate_threshold:float=10**-7) -> list[float]:
    x:float = start
    k = 0
    
    xs:list[float] = [x]
    last_f:float = float('inf')
    while abs(last_f - f(x)) > terminate_threshold:
        last_f = f(x)
        x -= f.df(x) * 1 / (k + 1)
        
        xs.append(x)
        k += 1
    
    return xs


if __name__ == '__main__':
    f:Function = Function()
    critical_point:list[float] = get_critical_point_with_gradient(f, 1/2)
    print(critical_point)
    plot_with_critical_point(f, xlim=(-5, 5), critical_point=critical_point, save_path='a.pdf')
