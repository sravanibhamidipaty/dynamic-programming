from typing import List

"""
What is the largest square that has its bottom right-corner at (r, c)?
If grid[r][c] == 1, the side length of the square ending there is:
1 + min(top, left, top-left)
"""

def maximalSquare_brute_force(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_side = 0

    def helper(r, c):
        nonlocal max_side
        # Base case: out of bounds or '0'
        if r < 0 or c < 0 or matrix[r][c] == "0":
            return 0

        side = 1 + min(helper(r-1, c), helper(r, c-1), helper(r-1, c-1))
        max_side = max(max_side, side)
        return side

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "1":
                helper(r, c)

    return max_side * max_side

"""
Time Complexity Brute Force: O(3 ^(M+N))
    - The Breakdown: Because there is no memoization, every single call to
    helper(r, c) triggers three new recursive calls.
    - This is an exponential growth pattern. In the worst case (a grid full of
    '1's), the number of redundant calculations is astronomical.
    - The recurrence relation is roughly T(N) = 3T(N-1), which simplifies to
    O(3^(path_length), or O(3^(M+N)).

Space Complexity: O(M + N)
    - The Breakdown: For the recursion stack.
    - The depth of the recursion tree is determined by the longest path from
    the bottom-right back to (0, 0), which is M + N steps.
    - Therefore, the space complexity is only the memory used by the call stack: O(M + N).
"""

def maximalSquare_memoization(matrix: List[List[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    memo = {}
    rows = len(matrix)
    cols = len(matrix[0])

    def helper(r, c):
        if r < 0 or c < 0 or matrix[r][c] == "0":
            return 0

        if (r, c) in memo:
            return memo[(r, c)]

        side = 1 + min(helper(r-1, c), helper(r, c-1), helper(r-1, c-1))

        memo[(r, c)] = side
        return memo[(r, c)]

    result = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "1":
                result = max(result, helper(r, c))

    return result

"""
Time Complexity: O(M x N)
1. Unique Subproblems: There are M x N cells in the matrix. Each cell is
represented by a unique pair o coordinates (r, c).
2. Memoization Effect: The helper function is designed to return the value
from the memo dictionary if it has already been computed.
3. Work per Cell: For each unique cell, the function performs a constant number
of operations: three recursive calls (which become O(1) lookups after the first
time), a min() calculation, and a dictionary insertion.
Total: Since each of the M x N cells is computer exactly one, the time
complexity is O(M x N).

Space Complexity: O(M x N)
1. Memoization Table: You are storing the result for every single cell in
the memo dictionary. In the worst case (a matrix full of '1's), this dictionary
will hold M x N entries.
2. Recursion Stack: The recursion depth is determined by the path taken
through the grid. The maximum depth of the call stack is O(M + N) (the longest
path from the bottom-right corner to the top-left).
3. Total: In Big-O notation, we combine these. Since M x N is always graeter
than or equal to the M + N for non-trivial grids, the space complexity is O(M x N)

Dry run:
matrix = [["1", "0"], ["1", "1"]]

helper(0, 0)
1 + min(0, 0, 0) = 1. memo = {(0, 0): 1}

helper(0, 1)
matrix is '0'. memo = {(0, 0): 1}

helper(1, 0)
1 + min(0, 0, 0) = 1. memo = {(0, 0): 1, (1, 0): 1}

helper(1, 1)
1 + min(helper(0, 1), helper(1, 0), helper(0, 0)) = 1 + min(0, 1, 1) = 1.
memo = {(0, 0): 1, (1, 0): 1, (1, 1): 1}
"""