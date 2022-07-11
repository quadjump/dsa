from functools import partial

class Infix(object):
    """
    Via https://www.tomerfiliba.com/blog/Infix-Operators
    """
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

"""
>>> @Infix
>>> ... def add(x, y):
>>> ...     return x + y
>>> ...
>>> 5 |add| 6
11
"""