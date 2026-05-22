from typing import List

"""
Time Complexity of the burte-force approach is O(2^n) time because of two
branches at each step, and O(n) space for the recursion stack.
"""
def rob_brute_force(nums: List[int]) -> int:
    def helper(i: int) -> int:
        # Base cases
        if i < 0:
            return 0
        if i == 0:
            return nums[0]

        # The recurrence relation: max(rob, skip)
        rob_current = helper(i - 2) + nums[i]
        skip_current = helper(i - 1)

        return max(rob_current, skip_current)

    # Start the recursion from the last house
    return helper(len(nums) - 1)

def rob_memo(nums: List[int]) -> int:
    memo = {}
    def helper(i: int) -> int:
        # Base cases
        if i < 0:
            return 0
        if i == 0:
            return nums[0]

        # Check cache
        if i in memo:
            return memo[i]

        # Compute and cache
        rob_current = helper(i - 2) + nums[i]
        skip_current = helper(i - 1)

        memo[i] = max(rob_current, skip_current)
        return memo[i]

    return helper(len(nums)-1)

def rob_tabulation(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # Initialize DP array
    dp = [0] * n

    # Base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Build bottom-up
    for i in range(2, n):
        # Recurrence Relation
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    return dp[n-1]

def rob_optimal(nums: List[int]) -> int:
    # rob1 is the max money if we rob up to house i-2
    # rob2 is the max money if we rob up to house i-1
    rob1 = 0
    rob2 = 0

    for money in nums:
        # Calculate the max we can get at the current house
        current_max = max(rob1 + money, rob2)

        # Shift our window forward for the next iteration
        rob1 = rob2
        rob2 = current_max

    return rob2

print(rob_brute_force([1,2,3,1]))
print(rob_memo([1,2,3,1]))
print(rob_tabulation([1,2,3,1]))
print(rob_optimal([1,2,3,1]))