def bisect_method_iteration(func, iteration, a, b):
    x0 = 0
    for i in range(iteration):
        x0 = (a + b) / 2
        if func(x0) * func(b) < 0:
            a = x0
        elif func(x0) * func(a) < 0:
            b = x0
    return x0


def bisect_method_accuracy(func, acc, a, b):
    x0 = (a + b) / 2
    if func(x0) == acc:
        return x0
    if func(x0) * func(b) < 0:
        a = x0
        bisect_method_accuracy(func, acc, a, b)
    elif func(x0) * func(a) < 0:
        b = x0
        bisect_method_accuracy(func, acc, a, b)
