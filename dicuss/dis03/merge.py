def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 < 10 and n2 < 10:
        if n1 >= n2:
            return 10 * n1 + n2
        else:
            return 10 * n2 + n1
    else:
        return 100 * merge(n1 // 10, n2 // 10) + merge(n1 % 10, n2 % 10)
    