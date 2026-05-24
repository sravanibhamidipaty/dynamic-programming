"""
Time Complexity: O(m x n)
- Explanation: You are filling a 2D table of size (m+1)x(n+1)
- Why: You have nested loops where the outer loop runs m times and the
inner loop runs n times. Each cell operation (comparison and assignment)
is O(1).

Space Complexity: O(m x n)
- Explanation: You are creating a 2D array (matrix) of size (m+1) x (n+1).

Dry Run:
word1 = "abc"
word2 = "ac"

We set up a DP table of size (m+1) x (n+1), which is 4x3.

DP Table Population
We initialize the first row and column to 0. As we iterate, we compare
characters at word1[i-1] and word2[j-1].

    ""  a   c
""  0   0   0
a   0   1   1
b   0   1   1
c   0   1   2

Step-by-Step Logic
1. Initialize: All cell in row 0 and column 0 are 0 because an empty
string comparison results in an LCS of 0.
2. i=1, j=1, ('a' vs. 'a'): They match. We take the value from the
diagonal (dp[0][0]), which is 0, and add 1. Result: 1.
3. i=1, j=2 ('a' vs 'c'): Mismatch. We take max(dp[0][2], dp[1][1]), which is
max(0, 1). Result: 1.
4. i=2, j=1 ('b' vs 'a'): Mismatch. We take max(dp[1][1], dp[2][0]), which is
max(1, 0). Result: 1.
5. i=2, j=2 ('b' vs 'c'): Mismatch. We take max([1][2], dp[2][1]), which is
max(1, 1). Result: 1.
6. i=3, j=1 ('c' vs 'a'): Mismatch. We take max(dp[2][1], dp[3][0]), which is
max(1, 0). Result: 1.
7. i=3, j=2 ('c' vs 'c'): Match. We take the diagonal value (dp[2][1]), which is
1, and add 1. Result 2.

The final value at dp[3][2] is 2, which is the length of the longest
common subsequence.
"""
def longest_common_subsequence(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]