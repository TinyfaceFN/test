def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    new_dict = {}
    for x in phrase:
        new_dict[x] =  phrase.count(x)
    print(new_dict)
    return new_dict

# multiple_letter_count('yay')