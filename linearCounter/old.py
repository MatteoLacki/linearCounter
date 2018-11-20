from collections import Counter

class linearCounter(Counter):
    def __add__(self, other):
        '''Add counts from two LinearCounters.

        >>> LinearCounter('abbb') + LinearCounter('bcc')
        Counter({'b': 4, 'c': 2, 'a': 1})

        >>> LinearCounter({'H':-4, 'Y':10}) + LinearCounter({'H=2','Z':3})
        LinearCounter({'H': -2, 'Y': 10, 'Z': 3})

        '''
        if not isinstance(other, linearCounter):
            return NotImplemented
        result = linearCounter()
        for elem, count in self.items():
            newcount = count + other[elem]
            result[elem] = newcount

        for elem, count in other.items():
            if elem not in self:
                result[elem] = count
        return result

    def __radd__(self, other):
        '''Add counts from two linearCounters.'''
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iadd__(self, other):
        '''Add counts from two linearCounters.'''
        if not isinstance(other, linearCounter):
            return NotImplemented
        for elem in self.keys():
            self[elem] += other[elem]
        for elem, count in other.items():
            if elem not in self:
                self[elem] = count
        return self

    def __isub__(self, other):
        '''Substracts counts from two LinearCounters.
        '''
        if not isinstance(other, linearCounter):
            return NotImplemented
        for elem in self.keys():
            self[elem] -= other[elem]
        for elem, count in other.items():
            if elem not in self:
                self[elem] = -count
        return self

    def __mul__(self, scalar):
        '''Multiplies the values stored in the linearCounter by the scalar.'''
        result = linearCounter()
        for elem, count in self.items():
            result[elem] = count*scalar
        return result

    def __rmul__(self, scalar):
        '''Multiplies the values stored in the linearCounter by the scalar.'''
        result = linearCounter()
        for elem, count in self.items():
            result[elem] = count*scalar
        return result
