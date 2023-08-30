def combination_sum(candidates, target):
    """
    Finds all the unique combinations of numbers in the candidates array that
    add up to target
    Inputs:
        candidates (list of ints): a list of integers
        target (int): the number to reach
    Returns: combinations (list of lists): a list of qualifying combinations
    """
    combinations = []
    
    def backtrack(start_index, combination, combination_sum=0):
        """
        Recursively adds combinations to the array that combination_sum() will
        return
        Inputs:
            start_index (int): index to start from in canidates array
            combination (list of ints): a combination
        Returns: None (modifies combinations in-place) 
        """
        if combination_sum == target:
            combinations.append(list(combination))
            return

        if combination_sum > target:
            return
        
        for i in range(start_index, len(candidates)):
            combination.append(candidates[i])
            combination_sum += candidates[i]
            backtrack(i, combination, combination_sum)
            combination.pop()
            combination_sum -= candidates[i]
    
    backtrack(0, [])
    return combinations

    


