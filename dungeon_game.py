def dungeon_game_brute_force(dungeon: list[list[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    rows = len(dungeon)
    cols = len(dungeon[0])

    def solve(r, c):
        # Base case: reached the bottom-right corner
        if r == rows - 1 and c == cols - 1:
            return max(1, 1 - dungeon[r][c])

        # Out of bounds
        if r >= rows or c >= cols:
            return float('inf')

        # Explore right and down
        right = solve(r, c+1)
        down = solve(r+1, c)

        # The knight needs the minimum of the two paths
        min_needed = min(right, down)

        # Calculate health needed at current cell
        return max(1, min_needed-dungeon[r][c])

    return solve(0, 0)

def dungeon_game_memoization(dungeon: list[list[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    rows = len(dungeon)
    cols = len(dungeon[0])
    memo = {}

    def solve(r, c):
        # Base case: reached the bottom-right corner
        if r == rows - 1 and c == cols - 1:
            return max(1, 1 - dungeon[r][c])

        # Out of bounds
        if r >= rows or c >= cols:
            return float('inf')

        if (r, c) in memo:
            return memo[(r, c)]

        # Explore right and down
        right = solve(r, c+1)
        down = solve(r+1, c)

        # The knight needs the minimum of the two paths
        min_needed = min(right, down)

        # Calculate health needed at current cell
        memo[(r, c)] = max(1, min_needed-dungeon[r][c])
        return memo[(r, c)]

    return solve(0, 0)