def length_of_longest_substring(s):
    """
    Finds the length of the longest substring without repeating characters
    Inputs:
        s (str): a string of characters
    Returns: longest_substr_len (int): length of longest distinct substring
    """
    longest_substr_len = 0
    left = 0
    right = 0
    seen = set()

    while right < len(s):
        if s[right] not in seen:
            seen.add(s[right])
            right += 1
            longest_substr_len = max(longest_substr_len, right - left)
        else:
            seen.remove(s[left])
            left += 1
        
    return longest_substr_len