from collections import Counter

def min_window(s, t):
    """
    Finds the minimum window substring of s such that every character in t 
    (including duplicates) exists in s
    Inputs:
        s (str): string to search
        t (str): string containing characters that must exist in minimum 
                window substring
    Returns: min_substr (str): the minimum substring window
    """
    if len(t) == 0:
        return ""
    
    min_substr_range = [0, 0]
    min_substr_len = float('inf')
    left = 0
    right = 0
    t_cnts = Counter(t)
    s_cnts = {}
    num_obtained = 0
    num_need = len(t_cnts)

    while right < len(s):
        s_cnts[s[right]] = s_cnts.get(s[right], 0) + 1

        if s[right] in t_cnts and s_cnts[s[right]] == t_cnts[s[right]]:
            num_obtained += 1
        
        while num_obtained == num_need:
            if (right - left + 1) < min_substr_len:
                min_substr_range = [left, right]
                min_substr_len = right - left + 1
            
            s_cnts[s[left]] -= 1

            if s[left] in t_cnts and s_cnts[s[left]] < t_cnts[s[left]]:
                num_obtained -= 1
            
            left += 1

        right += 1
    
    if min_substr_len == float('inf'):
        return ""
    
    start, end = min_substr_range
    min_substr = s[start:end + 1]
    return min_substr