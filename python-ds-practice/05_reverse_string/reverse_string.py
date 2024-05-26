def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_list = list(phrase)
    new_list.reverse()
    reverse_list = ''.join(new_list) 
    print(reverse_list)
    return reverse_list
# reverse_string('awesome')