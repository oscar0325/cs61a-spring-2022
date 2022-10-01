def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    m = 1
    def count(n, record):
        print(n)
        if n == 1:
            return record
        elif n % 2 == 0:
            return count(n // 2, record + 1)
        else:
            return count(n * 3 + 1, record + 1)
    return count(n, m)