def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, *u = line.split()
        ts.append(float(t))
        us.append(list(map(float, u)))
        
    return ts, us

def txt2tex1():
    ts, us = readfile('main.txt')
    
    chosen_u = []
    for t, u in zip(ts, us):
        if t == 1 or t == 2 or t == 3 or t == 4:
            chosen_u.append(u)
            
    print('')
    for i in range(len(chosen_u[0])):
        print(f'{i * 0.05 - 10.025:.3f} & {chosen_u[0][i]:.8f} & {chosen_u[1][i]:.8f} & {chosen_u[2][i]:.8f} & {chosen_u[3][i]:.8f} \\\\')
        
def txt2tex2():
    ts, us = readfile('main.txt')
    
    chosen_u = []
    for t, u in zip(ts, us):
        if t == 5 or t == 6 or t == 7 or t == 8:
            chosen_u.append(u)
            
    print('')
    for i in range(len(chosen_u[0])):
        print(f'{i * 0.05 - 10.025:.3f} & {chosen_u[0][i]:.8f} & {chosen_u[1][i]:.8f} & {chosen_u[2][i]:.8f} & {chosen_u[3][i]:.8f} \\\\')

if __name__ == '__main__':
    txt2tex1()
    txt2tex2()