# linearCounter

This is a Python module that extends the counters to any linear operations.
It's bloody simple.
Think of it as infinitely dimensional sparse array (hehe).

Example
-------

```Python
from linearCounter import LC

x = LC({'H':10, 'O':5})
y = LC({'H':10.2, 'O':5.1})
z = LC({'H':10.3, 'O':5.112, 'M':24232.232})

x += y
print(x)
# LC{'H': 20.2, 'O': 10.1}

x -= z
print(x)
# LC{'H': 9.899999999999999, 'O': 4.9879999999999995, 'M': -24232.232}

print(sum([x,y,z]))
# LC{'H': 30.4, 'O': 15.2}
# if a value for a key at some moment is set to 0, we forget about it!

print(x['Z'])
# by default, everything is set to zero.

print(x*100 + y)
# LC{'H': 1010.2, 'O': 505.1}
```
see - it just works.

Watch out
---------
It does not always just work.

Adding scalars is genuinely stupid in infinite dimensions.
But I thought, why not support it, to some extent.
The way addition works is like this:

```Python
from linearCounter import LC

x = LC({'H':10, 'O':5})
print(x + 10)
# LC{'H': 20, 'O': 15}
```
So, we only add to non-zero coordinates.
This makes the addition of scalar non-commutative for LCs with different keys!

```Python
from linearCounter import LC

x = LC({'H':10, 'O':5})
y = LC({'H':4, 'Z':5})
print(x + y + 5)
# LC{'H': 19, 'O': 10, 'Z': 10}
print(x + 5 + y)
# LC{'H': 19, 'O': 10, 'Z': 5}
# this means, that the brackets go like this ((x + 5) + y)
# and 5 did not got added to the missing Z-coordinate.
```
Pity? Well, I don't care, since there are still a lot of uses :)
