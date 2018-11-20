from operator import add, mul, truediv, sub, floordiv


class LinearCounter(dict):
    """A dictionary extended to linear operations.

    >>> LinearCounter({'H':-4, 'Y':10}) + LinearCounter({'H=2','Z':3})
        LinearCounter({'H': -2, 'Y': 10, 'Z': 3})
    """
    def __setitem__(self, key, value):
        if value == 0:
            del self[key]
        else:
            super().__setitem__(key, value)

    def __getitem__(self, key):
        return self.get(key, 0)

    def __add__(self, other):
        o = self.copy()
        return o if other == 0 else o.__do(other, add)

    def __sub__(self, other):
        o = self.copy()
        return o if other == 0 else o.__do(other, sub)

    def __mul__(self, other):
        o = self.copy()
        return o if other == 1 else o.__do(other, mul)

    def __truediv__(self, other):
        o = self.copy()
        if other == 1:
            return o
        elif other == inf:
            return o*0
        else:
            return o.__do(other, truediv)

    def __flooordiv__(self, other):
        o = self.copy()
        if other == 1:
            return o
        elif other == inf:
            return o*0
        else:
            return o.__do(other, floordiv)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rdiv__(self, other):
        return self.__div__(other)

    def __do(self, other, op):
        try:
            for k in set().union(self, other):
                self[k] = op(self[k], other[k])
            return self
        except KeyError:
            print("Coordinate-wise division works only if objects share keys.")
            raise
        except (TypeError, AttributeError):
            try:
                for k in list(self.keys()):
                    self[k] = op(self.get(k, 0), other)
                return self
            except (TypeError, AttributeError):
                print("Operation supported only for dict-like structures and scalars.")
                raise

    def __repr__(self):
        return "LD" + super().__repr__()

    def copy(self):
        return self.__class__(self)

LD({})
x = LD({"a": 10, "b": 30})
y = LD({"a": 11, "c": 3})
x + 2
x - 3
2 + x
'a' + x
x + y + 2
x*10 + 2.3
w = x * 0
x['d']
x*0
0*x
from math import inf
x / inf
x / y

x = LD()
x['a'] = 10
x['b'] += 23
x