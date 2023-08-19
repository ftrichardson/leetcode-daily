def maximum_subarray_sum(nums, k):
    """
    Finds the maximum subarray sum of all distinct subarrays of length k
    Inputs:
        nums (list of ints): subarray
        k (int): length of subarray
    Returns: max_subarray_sum (int) the maximum subarray sum given the 
            conditions
    """
    max_subarray_sum = 0
    current_sum = 0
    left = 0
    right = 0
    seen = set()

    while right < len(nums):
        if nums[right] not in seen:
            seen.add(nums[right])
            current_sum += nums[right]
            right += 1

            if right - left == k:
                max_subarray_sum = max(max_subarray_sum, current_sum)
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
        else:
            seen.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        
    return max_subarray_sum