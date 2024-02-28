def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    vow_loc = []
    lst = []
    for i in range(len(s)):
        if vowels.count(s[i]) == 1:
            vow_loc.append(i)
    vow_count = len(vow_loc)
    for i in range(len(s)):
        if i in vow_loc:
            lst.append(s[vow_loc[vow_count - vow_loc.index(i) - 1]])
        else:
            lst.append(s[i])
    return "".join(lst)
