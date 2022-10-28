from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 18


def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts = []
    for line in lines:
        ts.append(float(line))
        
    return ts


if __name__ == '__main__':
    fig = plt.figure(figsize=(6.4 * 2, 4.8))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    thetas1 = readfile('K1.txt')
    thetas3 = readfile('K3.txt')
    
    t = np.linspace(0, 2 * np.pi, 1000)
    ax1.plot(np.cos(t), np.sin(t), color='grey', linestyle=':')
    ax2.plot(np.cos(t), np.sin(t), color='grey', linestyle=':')
    
    ax1.set_aspect(1)
    ax2.set_aspect(1)
    
    ax1.set_xlabel('$\cos x_i$')
    ax1.set_ylabel('$\sin x_i$', rotation=0)
    ax2.set_xlabel('$\cos x_i$')
    ax2.set_ylabel('$\sin x_i$', rotation=0)
    
    ax1.scatter(np.cos(thetas1), np.sin(thetas1), color='black', zorder=10)
    ax2.scatter(np.cos(thetas3), np.sin(thetas3), color='black', zorder=10)
    
    for theta in thetas1:
        ax1.plot([0, np.cos(theta)], [0, np.sin(theta)], color='black')
    for theta in thetas3:
        ax2.plot([0, np.cos(theta)], [0, np.sin(theta)], color='black')
    
    
    plt.tight_layout()
    plt.savefig('K.eps')
    