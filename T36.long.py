def length_of_LIS(nums):
    if not nums:
        return 0
    
    # Initialize dp array where each element is at least 1
    dp = [1] * len(nums)
    
    # Fill the dp array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The length of the longest increasing subsequence is the max value in dp
    return max(dp)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Length of the longest increasing subsequence: {length_of_LIS(nums)}")
