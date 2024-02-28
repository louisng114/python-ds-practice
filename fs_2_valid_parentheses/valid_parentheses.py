def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    counter = 0
    for ltr in parens:
        if ltr == "(":
            counter += 1
        if ltr == ")":
            counter -= 1
            if counter < 0:
                return False
    if counter == 0:
        return True
    else:
        return False
