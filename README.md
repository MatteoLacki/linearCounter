# linearCounter

This is a Python module that extends the counters to any linear operations.

Listen, it's bloody simple. Think of a dictionary that has some arbitrary keys and values that can be added, substracted, and multiplied by a number (real/complex/very complex). Then you want to build up *sort of vectors* but with arbitrarily named entries and perform operation on these little buggers.

Example
-------

```Python
from linearCounter import linearCounter as lCnt

x = lCnt({'H':10, 'O':5})
y = lCnt({'H':10.2, 'O':5.1})
z = lCnt({'H':10.3, 'O':5.112, 'M':24232.232})

x += y
print(x)
# linearCounter({'H': 20.2, 'O': 10.1})

x -= z
print(x)
# linearCounter({'H': 9.899999999999999, 'M': -24232.232, 'O': 4.9879999999999995})

print(sum([x,y,z]))
# linearCounter({'H': 30.4, 'M': 0.0, 'O': 15.2})

# see - it works
```

Watch out
---------

Of course we have to always assume something:
* the dimensions that are unnamed will be assumed to be equal to zero.
> This is natural: whoever doesn't exist in a linear space should be assumed to be a 0.

*Presumably said by Hilbert while playing golf.*
