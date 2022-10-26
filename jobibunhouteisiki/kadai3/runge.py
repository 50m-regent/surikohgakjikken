from matplotlib import pyplot as plt

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 18


def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, u = line.split()
        ts.append(float(t))
        us.append(float(u))
        
    return ts, us


if __name__ == '__main__':
    fig = plt.figure(figsize=(6.4 * 2, 4.8))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    ts, us = readfile('runge_kutta.txt')
    
    ax1.plot(ts, us, color='black', marker='.')
    ax2.plot(ts, us, color='black', marker='.')
    
    ax1.set_xlabel('$\Delta t$')
    ax1.set_ylabel('$E$', rotation=0)
    ax2.set_xlabel('$\Delta t$')
    ax2.set_ylabel('$E$', rotation=0)
    
    # plt.xlim(1e-7, 1)
    # plt.ylim(1e-15, 1)
    
    ax1.set_yscale('log')
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    
    plt.tight_layout()
    
    plt.savefig('runge_kutta.eps')
    