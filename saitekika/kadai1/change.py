from matplotlib import pyplot

from function import Function, get_zero_points
from b import get_zero_point_with_bisection
from c import get_zero_point_with_newton


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def plot_zero_points(zero_points:dict[str, list[float]], save_path:int) -> None:
    pyplot.cla()
    
    markers = {
        'Bisection': 'o',
        'Newton': 'd'
    }
    
    longest = -float('inf')
    for algorithm, zero_point in zero_points.items():
        time = len(zero_point) + 1
        if longest < time:
            longest = time
        pyplot.scatter(list(range(1, time)), [abs(x - zero_point[-1]) + 10**-7 for x in zero_point], label=f'{algorithm}', marker=markers[algorithm])
    
    pyplot.xlim(-0.5, longest) 
    pyplot.yscale('log')
    
    pyplot.xlabel('$k$')
    pyplot.ylabel('$E$', rotation=0)
        
    pyplot.legend()
    pyplot.savefig(save_path)


if __name__ == '__main__':
    f:Function = Function()
    bisection_zero_points:list[float] = get_zero_points(get_zero_point_with_bisection, f, starts=[
        (-5, -2.5),
        (-2.5, 0),
        (0, 2.5)
    ])
    newton_zero_points:list[float] = get_zero_points(get_zero_point_with_newton, f, starts=[
        -4,
        0,
        4
    ])
    
    for i, (bisection_zero_point, newton_zero_point) in enumerate(zip(bisection_zero_points, newton_zero_points)):
        plot_zero_points({
            'Bisection': bisection_zero_point,
            'Newton': newton_zero_point
        }, save_path=f'change{i}.pdf')