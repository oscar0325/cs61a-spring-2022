def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond> and prints out
       all integers 1..i..n where calling cond(i) returns True. The returned
       function returns another function with the exact same behavior.

        >>> def multiple_of_4(x):
        ...     return x % 4 == 0
        >>> def ends_with_1(x):
        ...     return x % 10 == 1
        >>> k = make_keeper_redux(11)(multiple_of_4)
        4
        8
        >>> k = k(ends_with_1)
        1
        11
        >>> k
        <function do_keep>
    """
    # Paste your code for make_keeper here!
    def do_keep(func):
        i = 1
        while i <= n:
            if func(i):
                print(i)
            i += 1
        return make_keeper_redux(n)

    return do_keep


def multiple_of_4(x):
    return x % 4 == 0


def ends_with_1(x):
    return x % 10 == 1