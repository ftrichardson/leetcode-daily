def repeated_substring_pattern(s):
    """
    Finds if a string can be constructed by concatenating copies of one of its
    substrings
    Inputs:
        s (str): the string
    Returns: (bool): whether or not string is perfectly divisible by one of its
        substrings
    """
    for i in range(1, len(s) // 2 + 1):
        if len(s) % i == 0:
            substr = s[:i]
            if substr * (len(s) / len(substr)) == s:
                return True

    return False