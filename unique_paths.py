"""
The Brute Force Approach (Recursion)
This approach explores every single path by choosing to move either down
or right at every step. Time Complexity: O(2^(m+n)), as it recalculates paths
for the same cells repeatedly.
"""
def uniquePaths_brute_force(m: int, n: int) -> int:
    # Base Case: Reached the bottom-right corner
    if m == 1 or n == 1:
        return 1

    # Recursive Step: Sum of moving down and moving right
    return uniquePaths_brute_force(m-1, n) + uniquePaths_brute_force(m, n-1)

"""
We optimize the brute force by storing the result of each (m, n) pair in
a dictionary (cache) so we don't recompute it.
Time Complexity: O(m x n)
Space Complexity: O(m x n)
"""
def uniquePaths_memoization(m: int, n: int) -> int:
    # Initialize the cache inside the main function
    memo = {}

    def helper(r: int, c: int) -> int:
        # Base case: Reached the target
        if r == 1 or c == 1:
            return 1

        # Check cache before calculating
        if (r, c) in memo:
            return memo[(r, c)]

        # Recursive step: memoize and return
        memo[(r, c)] = helper(r-1, c) + helper(r, c-1)
        return memo[(r, c)]

    return helper(m, n)

"""
Instead of recursion, we build a 2D table where dp[i][j] is the number of ways
to reach that cell.
Time Complexity: O(m x n)
Space Complexity: O(m x n)
"""
def uniquePaths_tabulation(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

"""
Notice that we only ever look at the current row and the row directly above it.
We can reduce the space to just one row.
Time Complexity: O(m x n)
Space Complexity: O(n)
"""
def uniquePaths_optimal(m: int, n: int) -> int:
    row = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            # The current cell becomes its current value (above)
            # plus the value of its left
            row[j] += row[j-1]

    return row[n-1]