def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    ltr_set = set(phrase)
    count_dict = {ltr : 0 for ltr in ltr_set}
    for ltr in phrase:
        count_dict[ltr] += 1
    return count_dict