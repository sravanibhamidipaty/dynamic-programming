"""
Definition: dp[i][j] is the minimum number of operations to transform
word1[0...i-1] into word2[0...j-1].
Base Cases: dp[i][0] is i (deleting all characters) and dp[0][j] is (inserting
all characters).

Time Complexity: O(m x n)
    - You visit each cell in the m x n matrix exactly once, and each
    operation inside the loop is O(1).

Space Complexity: O(m x n)
    - You are using a 2D array of size (m+1) x (n+1)

Dry Run word1 = "horse", word2 = "ros"
        ""  r   o   s
""      0   1   2   3
h       1   1   2   3
ho      2   2   1   2
hor     3   2   2   2
hors    4   3   3   3
horse   5   4   4   3

If characters match: dp[i][j] = dp[i-1][j-1] (No cost added).
If characters don't match: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1],
dp[i-1][j-1])
    - dp[i-1][j] represents a deletion from word1.
    - dp[i][j-1] represents an insertion into word1.
    - dp[i-1][j-1] represents a replacement of a character.
"""

def minDistance(self, word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i

    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

    return dp[m][n]