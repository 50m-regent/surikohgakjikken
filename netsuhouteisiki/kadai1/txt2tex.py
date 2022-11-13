def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, *u = line.split()
        ts.append(float(t))
        us.append(list(map(float, u)))
        
    return ts, us

def txt2tex1(path):
    ts, us = readfile(path)
    
    chosen_u = []
    for t, u in zip(ts, us):
        if t == 1 or t == 2 or t == 3 or t == 4 or t == 5:
            chosen_u.append(u)
            
    print('')
    for i in range(len(chosen_u[0])):
        print(f'{i * 0.5 - 0.25:.2f} & {chosen_u[0][i]:.6f} & {chosen_u[1][i]:.6f} & {chosen_u[2][i]:.6f} & {chosen_u[3][i]:.6f} & {chosen_u[4][i]:.6f} \\\\')
        
def txt2tex2(path):
    ts, us = readfile(path)
    
    chosen_u = []
    for t, u in zip(ts, us):
        if t == 1 or t == 2 or t == 3 or t == 4 or t == 5:
            chosen_u.append(u)
            
    print('')
    for i in range(len(chosen_u[0])):
        print(f'{i * 0.05 - 0.025:.3f} & {chosen_u[0][i]:.6f} & {chosen_u[1][i]:.6f} & {chosen_u[2][i]:.6f} & {chosen_u[3][i]:.6f} & {chosen_u[4][i]:.6f} \\\\')

if __name__ == '__main__':
    txt2tex1('1.txt')
    txt2tex1('2.txt')
    txt2tex2('3.txt')
    txt2tex2('4.txt')