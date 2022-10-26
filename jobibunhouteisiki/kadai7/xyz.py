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
    fig = plt.figure()
    
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel("$x(t)$")
    ax.set_ylabel("$y(t)$")
    ax.set_zlabel("$z(t)$")
    
    ax.xaxis.set_rotate_label(False)
    ax.yaxis.set_rotate_label(False)
    ax.zaxis.set_rotate_label(False)
    
    t, x = readfile('x.txt')
    t, y = readfile('y.txt')
    t, z = readfile('z.txt')
    
    ax.plot(x, y, z, color='black')
    
    plt.tight_layout()
    plt.savefig('xyz.eps')
    