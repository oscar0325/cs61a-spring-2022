def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"

    num_a = next(a)
    num_b = next(b)
    while True:
        if num_a < num_b:
            yield num_a
            num_a = next(a)
        elif num_a == num_b:
            yield num_a
            num_a = next(a)
            num_b = next(b)
        else:
            yield num_b
            num_b = next(b)



