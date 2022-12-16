import numpy
from matplotlib import pyplot

from function import Function, get_zero_points, plot_with_zero_points


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def get_zero_point_with_bisection(f:Function, start:tuple[float], terminate_threshold:float=10**-7) -> list[float]:
    left:float
    right:float
    left, right = start
    
    assert f(left) * f(right) <= 0
    
    mid:float = None
    mids:list[float] = []
    while abs(left - right) > terminate_threshold:
        mid = (left + right) / 2
        mids.append(mid)
        if f(mid) * f(left) > 0:
            left = mid
        else:
            right = mid
            
    mids.append(mid)
    return mids


if __name__ == '__main__':
    f:Function = Function()
    zero_points:list[float] = get_zero_points(get_zero_point_with_bisection, f, starts=[
        (-5, -2.5),
        (-2.5, 0),
        (0, 2.5)
    ])
    print(zero_points)
    plot_with_zero_points(f, xlim=(-10, 10), ylim=(-10, 10), zero_points=zero_points, save_path='b.pdf')
