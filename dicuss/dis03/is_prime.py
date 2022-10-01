def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def is_factor(x):
        if x >= n:
            return True
        if x < n and n % x == 0:
            return False
        else:
            return is_factor(x+1)
    return is_factor(2)