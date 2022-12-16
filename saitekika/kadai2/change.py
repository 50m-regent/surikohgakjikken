from matplotlib import pyplot

from function import Function
from a import get_critical_point_with_gradient
from b import get_critical_point_with_newton


pyplot.rcParams["text.usetex"] = True
pyplot.rcParams["font.size"] = 12


def plot_critical_points(critical_points:dict[str, list[float]], save_path:int) -> None:
    longest = -float('inf')
    for algorithm, critical_point in critical_points.items():
        time = len(critical_point) + 1
        if longest < time:
            longest = time
        pyplot.scatter(list(range(1, time)), [abs(x - critical_point[-1]) + 10**-7 for x in critical_point], label=f'{algorithm}')
    
    pyplot.xlim(-0.5, longest) 
    pyplot.yscale('log')
        
    pyplot.legend()
    pyplot.savefig(save_path)


if __name__ == '__main__':
    f:Function = Function()
    gradient_critical_point:list[float] = get_critical_point_with_gradient(f, 1/2)
    newton_critical_point:list[float] = get_critical_point_with_newton(f, 5)
    
    plot_critical_points({
        'Gradient': gradient_critical_point,
        'Newton': newton_critical_point
    }, save_path=f'change.pdf')