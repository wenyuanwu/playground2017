def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    street_a, avenue_a = street(a), avenue(a)
    street_b, avenue_b = street(b), avenue(b)
    return abs(street_a- street_b) + abs(avenue_a - avenue_b)

# times_square = intersection(46, 7)
# ess_a_bagel = intersection(51, 3)
# print(taxicab(times_square, ess_a_bagel))
# print(taxicab(ess_a_bagel, times_square))

def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [int(x**0.5) for x in s if int(x**0.5) == (x**0.5)]
seq = [500, 30]
print(squares(seq))