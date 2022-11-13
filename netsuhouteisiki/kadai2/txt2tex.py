def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, *u = line.split()
        ts.append(float(t))
        us.append(list(map(float, u)))
        
    return ts, us

def txt2tex(path):
    ts, us = readfile(path)
    
    chosen_u = []
    for t, u in zip(ts, us):
        if t == 10 or t == 20 or t == 30 or t == 40:
            chosen_u.append(u)
            
    print('')
    for i in range(len(chosen_u[0])):
        if 1 < i * 0.05 - 0.025 and 99 > i * 0.05 - 0.025 or 101 < i * 0.05 - 0.025 and 199 > i * 0.05 - 0.025:
            continue
        print(f'{i * 0.05 - 0.025:.3f} & {chosen_u[0][i]:.6f} & {chosen_u[1][i]:.6f} & {chosen_u[2][i]:.6f} & {chosen_u[3][i]:.6f} \\\\')

if __name__ == '__main__':
    txt2tex('25.txt')
    txt2tex('50.txt')
    txt2tex('100.txt')