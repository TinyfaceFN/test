def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    list_phrase = list(phrase)
    new_phrase = []
    for letter in list_phrase:
        if letter.upper() == to_swap.upper():
            if letter == letter.upper():
                new_phrase.append(letter.lower())
            else:
                new_phrase.append(letter.upper())
        else:
            new_phrase.append(letter)        
    print(''.join(new_phrase))
    return ''.join(new_phrase)