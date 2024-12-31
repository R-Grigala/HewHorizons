def x2(x):
    return f'{x} * {x} = {x**2}'

def x10(x):
    return f'{x} ^ 10 = {x**10}'

def xx(x):
    return f'{x} ^ {x} = {x**x}'

for x in range(1, 16):
    x_2 = x2(x)
    x_10 =x10(x)
    x_x = xx(x)
    print(f'{x_2} | {x_10} | {x_x}' )