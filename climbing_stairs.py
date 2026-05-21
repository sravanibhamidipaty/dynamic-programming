"""
1. Clarify and Define Constraints
Don't jump straight into coding.
- "Can n be zero or negative?" (Usually, n >= 1. If n = 0, is the answer 0 or 1 way?
Standard is 1 way to stand still).
- "Are we restricted to strictly 1 or 2 steps?" (This sets you up for the inevitable
follow-up).

Think Out Loud: The Optimization Journey
- Approach 1: Brute Force (Recursion)
    - Explanation: At step i, we can either take 1 step to i+1 or 2 steps to
    i+2. We can represent this as a decision tree.
    - Complexity: O(2^n) time, O(n) space (call stack). Mention this is too slow.
- Approach 2: Top-Down Dynamic Programming (Memoization)
    - Explanation: We are recalculating the same subproblems. We can cache the results
    of climbStairs(i) in an array or hash map.
    - Complexity: O(n) time, O(n) space.
- Approach 3: Bottom-Up Dynamic Programming (Tabulation)
    - Explanation: Instead of recursion, use an array of size n + 1 where
    dp[i] = dp[i-1] + dp[i-2].
    - Complexity: O(n) time, O(n) space.
- Approach 4: Constant Space DP
    - Explanation: Notice that dp[i] only ever depends on the last two steps.
    We don't need a whole array; we just need two variables.
    - Complexity: O(n) time, O(1) space.
"""

def climbStairs_brute_force(n: int) -> int:
    # Base cases:
    # 0 ways to climb negative stairs
    if n < 0:
        return 0
    # 1 way to stay at the ground (0 stairs) or 1st stair
    if n == 0 or n == 1:
        return 1

    # The recurrence relation
    return climbStairs_brute_force(n-1) + climbStairs_brute_force(n-2)

def climbStairs_memoization(n: int) -> int:
    # Initialize a cache (dictionary) to store computed results
    memo = {0: 1, 1: 1}

    def helper(step: int) -> int:
        # If we have already solved this subproblem, return the cached result
        if step in memo:
            return memo[step]

        # Otherwise, compute, cache, and return
        memo[step] = helper(step-1) + helper(step-2)
        return memo[step]

    return helper(n)

def climbStairs_tabulation(n: int) -> int:
    if n <= 1:
        return 1

    # Create an array to store the number of ways to reach each step
    dp = [0] * (n+1)

    # Base cases
    dp[0] = 1
    dp[1] = 1

    # Build the solution bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def climbStairs_optimal(n: int) -> int:
    if n <= 1:
        return 1

    # Variables to track the last two steps
    two_steps_back = 1 # Equivalent to dp[0]
    one_step_back = 1 # Equivalent to dp[1]

    for _ in range(2, n+1):
        current_ways = one_step_back + two_steps_back

        # Shift our "window" of two variables forward
        two_steps_back = one_step_back
        one_step_back = current_ways

    return one_step_back

print(climbStairs_brute_force(3))
print(climbStairs_memoization(3))
print(climbStairs_tabulation(3))
print(climbStairs_optimal(3))