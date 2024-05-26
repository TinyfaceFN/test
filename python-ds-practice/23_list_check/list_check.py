def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    is_all_list = True
    for thing in lst:
        if type(thing) is not list:
            is_all_list = False
    return is_all_list