from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 18
plt.rcParams['figure.figsize'] = (5, 5)


def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts = []
    for line in lines:
        ts.append(float(line))
        
    return ts


def plot_thetas(thetas, savepath):
    plt.cla()
    
    t = np.linspace(0, 2 * np.pi, 1000)
    plt.plot(np.cos(t), np.sin(t), color='grey', linestyle=':')
    plt.scatter(np.cos(thetas), np.sin(thetas), color='black', zorder=10)
    for theta in thetas:
        plt.plot([0, np.cos(theta)], [0, np.sin(theta)], color='black')
    
    plt.gca().set_aspect('equal')
    
    plt.xlabel('$x$')
    plt.ylabel('$y$', rotation=0)
    
    plt.tight_layout()
    plt.savefig(savepath)


if __name__ == '__main__':
    plot_thetas(readfile('K1.txt'), 'K1.eps')
    plot_thetas(readfile('K3.txt'), 'K3.eps')
    plot_thetas(readfile('K5.txt'), 'K5.eps')
    plot_thetas(readfile('K10.txt'), 'K10.eps')
    