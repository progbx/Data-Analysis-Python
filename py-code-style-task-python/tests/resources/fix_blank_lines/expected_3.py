import math


def f(x):
    return math.log(x)


class Wrapper:
    def __init__(self, func):
        self.func = func
    def __call__(self, x):
        return self.func(x)
