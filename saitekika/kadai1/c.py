from matplotlib import pyplot

from function import Function, get_zero_points, plot_with_zero_points


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def get_zero_point_with_newton(f:Function, start:float, terminate_threshold:float=10**-7) -> list[float]:
    x:float = start
    xs:list[float] = []
    while abs(f(x)) > terminate_threshold:
        xs.append(x)
        x -= f(x) / f.df(x)
        
    xs.append(x)
    return xs


if __name__ == '__main__':
    f:Function = Function()
    zero_points:list[float] = get_zero_points(get_zero_point_with_newton, f, starts=[
        -2.5,
        0,
        2.5
    ])
    plot_with_zero_points(f, xlim=(-10, 10), ylim=(-10, 10), zero_points=zero_points, save_path='c.pdf')