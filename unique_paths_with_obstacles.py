"""
Brute Force (Recursion)
In the recursive approach, we add a base case: if the current cell (r, c)
is an obstacle, return 0.
"""
def uniquePaths_obstacles_brute_force(grid, r, c):
    # Check bounds and obstacle
    if r < 0 or c < 0 or grid[r][c] == 1:
        return 0

    # Base case: reached origin:
    if r == 0 and c == 0:
        return 1

    return uniquePaths_obstacles_brute_force(grid, r-1, c) + uniquePaths_obstacles_brute_force(grid, r, c-1)

"""
Memoization (Top-Down)
We pass the grid to the helper and treat any cell with grid[r][c] == 1 as returning
0 paths.
"""
def uniquePaths_obstacles_memoization(grid):
    m = len(grid)
    n = len(grid[0])
    memo = {}

    def helper(r, c):
        if r < 0 or c < 0 or grid[r][c] == 1:
            return 0
        if r == 0 and c == 0:
            return 1
        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = helper(r-1, c) + helper(r, c-1)
        return memo[(r, c)]
    return helper(m-1, n-1)

"""
We iterate through the grid. If a cell is an obstacle, we set dp[i][j] = 0.
Otherwise, we sum the valid paths from the top and left.
"""
def uniquePaths_obstacles_tabulation(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Starting point initialization
    dp[0][0] = 1 if grid[0][0] == 0 else 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0: dp[i][j] += dp[i-1][j]
            if j > 0: dp[i][j] += dp[i][j-1]

    return dp[m-1][n-1]

"""
Space-Optimized (1D DP)
"""
def uniquePaths_obstacles_optimal(grid):
    m = len(grid)
    n = len(grid[0])
    row = [0] * n
    row[0] = 1 if grid[0][0] == 0 else 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                row[j] = 0
            elif j > 0:
                row[j] += row[j-1]

    return row[n-1]