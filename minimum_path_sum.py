def min_path_sum_brute_force(grid):
    rows = len(grid)
    cols = len(grid[0])

    def helper(r, c):
        if r < 0 or c < 0:
            return float('inf')

        if r == 0 or c == 0:
            return grid[r][c]

        return grid[r][c] + min(grid[r-1][c], grid[r][c-1])

    result = helper(rows-1, cols-1)
    return result if result != float('inf') else -1

def min_path_sum_memoization(grid):
    rows = len(grid)
    cols = len(grid[0])

    memo = {}

    def helper(r, c):
        if r < 0 or c < 0:
            return float('inf')

        if r == 0 and c == 0:
            return grid[0][0]

        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = grid[r][c] + min(helper(r-1, c), helper(r, c-1))
        return memo[(r, c)]

    result = helper(rows-1, cols-1)
    return result if result != float('inf') else -1

"""
grid = [[1, 3], [1, 2]]

helper(1, 1)
2 + min(helper(0, 1), helper(1, 0))
Needs helper(0, 1) and helper(1, 0)
memo = {}

helper(0, 1)
3 + min(helper(-1, 1), helper(0, 0))
Needs helper(-1, 1) and helper(0, 0)
memo = {}

helper(-1, 1)
Out of bounds
return float('inf')

helper(0, 0)
Base case returns 1

helper(0, 1)
3 + min(inf, 1) = 4
Returns 4
memo = {(0, 1): 4}

helper(1, 0)
Needs helper(0, 0) and helper(1, -1)

helper(0, 0)
Base case returns 1

helper(1, -1)
Out of bounds
return float('inf')

helper(1, 0)
1 + min(1, inf) = 2
memo = {(0, 1): 4, (1, 0): 2}

helper(1, 1)
2 + min(4, 2) = 4
memo = {(0, 1): 4, (1, 0): 2, (1, 1): 4}

Returns 4

Time Complexity: O(M x N)
    - In a grid of size M x N, there are exactly M x N unique coordinates.
    - Because of your memo dictionary, each coordinate (r, c) is computer only once.
    - After the first time a specific (r, c) is calculated, all subsequent calls for that coordinate are O(1) dictionary lookups.
    - Therefore, the total time is proportional to the number of calls.
    
Space Complexity: O(M x N)
    - There are two components to space complexity in top-down recursion
        1. The Memoization Table: You store an entry for every cell in the grid,
        which takes O(M x N) space.
        2. The Call Stack: The recursion depth (the maximum number of frames on the stack)
        will be O(M + N), as the longest path from (M-1, N-1) back to (0, 0) is M + N steps.
    - In Big-O notation, we take the dominant term: O(M x N) + O(M + N) -> O(M x N).
"""