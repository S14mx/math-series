def fibonacci(n: int) -> int:
    """Take in an integer and return the nth value in Fibonacci sequence

    Args:
        n (int): negative integer will result in an error

    Returns:
        int: nth value in Fibonacci sequence
    """
    if n < 0:
        return "Invalid Input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n: int) -> int:
    """Take in an integer and return the nth value in Lucas sequence

    Args:
        n (int): negative integer will result in an error

    Returns:
        int: nth value in Lucas sequence
    """
    if n < 0:
        return "Invalid Input"
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n: int, first=0, second=1) -> int:
    """Take in an integer and return the nth value in a sequence. Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series

    Args:
        n (int): negative integer will result in an error
        first (int, optional): determines first value in the sequence to be produced. Defaults to 0.
        second (int, optional): determines second value in the sequence to be produced. Defaults to 1.

    Returns:
        int: Then nth value of the proper sequence
    """
    if n < 0:
        return "Invalid Input"
    elif n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)
