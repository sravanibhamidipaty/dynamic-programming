from typing import List

def minCostClimbingStairs_brute_force(cost: List[int]) -> int:
    n = len(cost)

    def helper(i: int) -> int:
        # Base cases
        if i < 0:
            return 0
        if i == 0 or i == 1:
            return cost[i]

        # Recurrence relation
        return cost[i] + min(helper(i-1), helper(i-2))

    # To reach the "top", we can come from the last step or the second to last
    return min(helper(n-1), helper(n-2))

def minCostClimbingStairs_memoization(cost: List[int]) -> int:
    n = len(cost)
    memo = {}

    def helper(i: int) -> int:
        # Base cases
        if i < 0:
            return 0

        if i == 0 or i == 1:
            return cost[i]

        # Check cache
        if i in memo:
            return memo[i]

        # Recurrence: current cost + min of previous two steps
        memo[i] = cost[i] + min(helper(i-1), helper(i-2))
        return memo[i]

    # The answer is the min cost to finish from either of the last two steps
    return min(helper(n-1), helper(n-2))

def minCostClimbingStairs_tabulation(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * (n+1)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return min(dp[n-1], dp[n-2])

def minCostClimbingStairs_optimal(cost: List[int]) -> int:
    # We can start at index 0 or index 1, so the "cost to reach"
    # those steps is just the cost of those steps themselves.
    first = cost[0]
    second = cost[1]

    # We start iterating from the 3rd step (index 2)
    for i in range(2, len(cost)):
        # The cost to reach current step 'i' is its own cost
        # plus the minimum cost to have reached either of the two previous steps
        current = cost[i] + min(first, second)

        # Shift the window forward
        first = second
        second = current

    # The top is reached from either of the last two steps.
    return min(first, second)

print(minCostClimbingStairs_brute_force([10, 15, 20]))
print(minCostClimbingStairs_memoization([10, 15, 20]))
print(minCostClimbingStairs_tabulation([10, 15, 20]))
print(minCostClimbingStairs_optimal([10, 15, 20]))