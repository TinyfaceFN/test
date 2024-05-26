def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_phrase = phrase.capitalize()
    print(new_phrase)
    return new_phrase
# capitalize('only first word')