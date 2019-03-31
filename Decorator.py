def dd(func):
    def dd1(*args, **kwargs):
        print(f'function name is {func.__name__}')
        print(f'*arg has {args} and **kwargs has {kwargs}')
        result = func(*args, **kwargs)
        return result
    return dd1


@dd
def cc(greet, name=None):
    return greet + ',' + name + '.'


print(cc('hi', name='Tom'))
