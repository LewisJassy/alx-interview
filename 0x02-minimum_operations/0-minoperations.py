#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters in the file.
    
    The allowed operations are:
    - Copy All: Copy all the characters present in the file.
    - Paste: Paste the copied characters.
    
    Args:
    n (int): The target number of 'H' characters.
    
    Returns:
    int: The minimum number of operations required to achieve exactly n 'H' characters.
         If n is impossible to achieve, returns 0.
    
    Example:
    >>> minOperations(9)
    6
    
    Explanation:
    H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
    Number of operations: 6
    """
    
    # If n is less than or equal to 1, it's impossible to achieve more than 1 'H'
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    # Loop to factorize n and count the operations
    while n > 1:
        # Check if the current divisor is a factor of n
        while n % divisor == 0:
            # If it is, increment the operations count by the divisor
            operations += divisor
            # Divide n by the divisor to reduce it
            n //= divisor
        # Move to the next possible divisor
        divisor += 1
    
    return operations
