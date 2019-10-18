def get_fib(pos):
    if pos == 0:
        return 0;
    elif pos == 1:
        return 1
    else:
        return get_fib(pos-1) + get_fib(pos-2)


print(get_fib(0))
print(get_fib(1))
print(get_fib(2))
print(get_fib(3))
print(get_fib(4))
print(get_fib(5))
print(get_fib(6))