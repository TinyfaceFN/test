def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    x = 1
    new_list = []
    while x<len(lst)+1:
        if x%2:
            new_list.append(lst[x-1])
        x+=1
    return new_list

