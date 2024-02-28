def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_lst = list(phrase)
    phrase_lst.reverse()
    return "".join(phrase_lst)