def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    list_phrase = list(phrase)
    list_phrase.reverse()
    list_phrase = ''.join(list_phrase)
    if list_phrase == phrase:
        print('is palindrome')
        return True
    else:
        print('not palindrome')
        return False

# is_palindrome('tacocat')
# is_palindrome('robert')