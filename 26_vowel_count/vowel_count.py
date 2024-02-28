def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    count_dict = {}
    low_phrase = phrase.lower()
    vowels = "aeiou"
    for ltr in low_phrase:
        if vowels.find(ltr) != -1:
            if ltr in count_dict.keys():
                count_dict[ltr] += 1
            else:
                count_dict[ltr] = 1
    return count_dict
