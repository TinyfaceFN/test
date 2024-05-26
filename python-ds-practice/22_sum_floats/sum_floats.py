def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    float_nums = []
    for num in nums:
        if type(num) is float:
            float_nums.append(num)
    total = 0
    for number in float_nums:
        total += number
    return total  
    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
