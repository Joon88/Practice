def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(consFunc):
    def func(a, b):
        return a
    pairFunc = consFunc
    return pairFunc(func)


def cdr(consFunc):
    def func(a, b):
        return b
    return consFunc(func)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))