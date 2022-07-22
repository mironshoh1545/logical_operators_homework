def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x1 = n // 10000
    x2 = n // 1000 % 10
    x3 = n // 100 % 10
    x4 = n // 10 % 10
    x5 = n % 10
    sum = x1 + x2 + x3 + x4 + x5
    return (x1 == 1 and 5 - sum < 3) or (x2 == 1 and x1 != 1 and 4 - sum < 2) or (x3 == 1 and x2 != 1 and x1 != 1 and 3 - sum < 2) or (x4 == 1 and x3 != 1 and x2 != 1 and x1 != 1 and 2 - sum == 0) or (x4 != 1 and x3 != 1 and x2 != 1 and x1 != 1 and sum == 1)