def f(x):
    if x < 0:
        x += 1
        if x < 0:
            return (-x) ** 3
    return x


f(-100)
