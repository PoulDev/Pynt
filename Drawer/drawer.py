drawers = {}

def drawer(shape):
    def inner(func):
        print(f'function {func.__name__} has been connected to {shape}')
        drawers[shape] = func
        return func
    return inner

