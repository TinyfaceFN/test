def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_list = []
    for thing in lst:
        if thing:
            new_list.append(thing)
    print(new_list)
    return new_list
# compact([0, 1, 2, '', [], False, (), None, 'All done'])