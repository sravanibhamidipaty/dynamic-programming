from typing import List

"""
For the Triangle problem (finding the minimum path sum from top to bottom),
the brute force approach involves exploring every possible path from the
top to the base. At each step, you have two choices: go to the "same index"
or the "index + 1" in the next row.

Dry Run (Small Example)
triangle = [[2], [3, 4], [6, 5, 7]]
1. helper(0, 0) calls helper(1, 0) and helper(1, 1).
2. helper(1, 0) calls helper(2, 0) and helper(2, 1).
    - Returns 3 + min(6, 5) = 8.
3. helper(1, 1) calls helper(2, 1) and helper(2, 2).
    - Returns 4 + min(5, 7) = 9.
4. helper(0, 0) returns 2 + min(8, 9) = 10.

Time and Space Complexity
    - Brute Force Time: O(2^(N)) where N is the number of rows (because each
    mode branches twice).
    - Memoized Time: O(N^2) because there are exactly N^2/2 cells in the triangle,
    and we visit each one exactly once.
    - Space: O(N^2) for the memo dictionary + O(N) for the recursion stack depth.
"""

def minimumTotal_brute_force(triangle: List[List[int]]) -> int:
    # row: current row index, col: current column index

    def helper(row, col):
        # Base Case: If we reach the last row, return the value
        if row == len(triangle)-1:
            return triangle[row][col]

        # Brute Force: explore both possible moves in the next row
        # Move 1: Same index (col)
        # Move 2: Next index (col + 1)
        path1 = helper(row+1, col)
        path2 = helper(row+1, col+1)

        return triangle[row][col] + min(path1, path2)

    return helper(0, 0)

def minimumTotal_memoization(triangle: List[List[int]]) -> int:
    memo = {}

    def helper(row, col):
        if row == len(triangle)-1:
            return triangle[row][col]
        if (row, col) in memo:
            return memo[(row, col)]

        memo[(row, col)] = triangle[row][col] + min(helper(row+1, col), helper(row+1, col+1))

        return memo[(row, col)]

    return helper(0, 0)