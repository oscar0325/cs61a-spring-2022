def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    k = 1
    while k <= n:
        if k % 3 == 0:
            if k % 5 == 0:
                print('fizzbuzz')
            else:
                print('fizz')
        elif k % 5 == 0:
            print('buzz')
        else:
            print(k)
        k += 1