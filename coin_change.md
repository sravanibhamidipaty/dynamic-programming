# Coin Change - Minimum Coins
**Problem:** Given coins and amount, return the minimum number of coins needed
to make amount. Return -1 if impossible.

**Example:** amount = 11, coins = [1, 2, 5] -> 3 (because 5 + 5 + 1)

**Core Idea (DP)**

dp[amt] = minimum coins to form amt.

For any amount, try each coin and take the best: 
dp[amt] = min(1 + dp[amt - coin]) for each coin <= amt

**Dry Run (amount = 6, coins = [1, 2, 5])**

amt = 1
- coin=1 -> 1 + dp[0]
- coin=2 -> skip (2 > 1)
- coin=5 -> skip (5 > 1)
- dp[1] = 1

amt = 2
- coin=1 -> 1 + dp[1]
- coin=2 -> 1 + dp[0]
- coin=5 -> skip (5 > 2)
- dp[2] = min(1+dp[1], 1+dp[0]) = 1

amt = 3
- coin=1 -> 1 + dp[2]
- coin=2 -> 1 + dp[1]
- coin=5 -> skip (5 > 3)
- dp[3] = min(1+dp[2], 1+dp[1]) = 2

amt = 4
- coin=1 -> 1 + dp[3]
- coin=2 -> 1 + dp[2]
- coin=5 -> skip (5 > 4)
- dp[4] = min(1+dp[3], 1+dp[2]) = 2

amt = 5
- coin=1 -> 1 + dp[4]
- coin=2 -> 1 + dp[3]
- coin=5 = 1 + dp[0]
- dp[5] = min(1+dp[4], 1+dp[3], 1+dp[0]) = 1

amt = 6
- coin=1 -> 1 + dp[5]
- coin=2 -> 1 + dp[4]
- coin=5 -> 1 + dp[1]
- dp[6] = min(1+dp[5], 1+dp[4], 1+dp[1]) = 2

**Bottom-Up DP**
```python
from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    
    for amt in range(1, amount+1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], 1 + dp[amt-coin])
    
    return dp[amount] if dp[amount] != float('inf') else -1
```
TC: O(amount * len(coins))

SC: O(amount)

**Brute Force**
```python
from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    def helper(amount):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        
        minCoins = float('inf')
        for coin in coins:
            result = helper(amount-coin)
            if result != float('inf'):
                minCoins = min(minCoins, result+1)

        return minCoins
    
    result = helper(amount)
    return result if result != float('inf') else -1
```

**Top-Down with Memoization**
```python
from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    memo = {}
    def helper(amount):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        
        minCoins = float('inf')
        for coin in coins:
            result = helper(amount - coin)
            if result != float('inf'):
                minCoins = min(minCoins, result + 1)
        
        memo[amount] = minCoins
        return memo[amount]
    
    result = helper(amount)
    return result if result != float('inf') else -1
```

# Coin Change II
**Problem:** Given coins and amount, return the total number of distinct
combinations that sum to amount. (Order doesn't matter - 1+2 and 2+1 are the same.)

**Example:** amount = 5, coins= [1, 2, 5] -> 4
- 5
- 2 + 2 + 1
- 2 + 1 + 1 + 1
- 1 + 1 + 1 + 1 + 1

**Key Insight: Avoiding Duplicate Combinations**

If we loop coins in the inner loop, we count permutations (1+2 and 2+1 separately). To count
combinations, iterate coin in the outer loop so each coin is considered in a fixed order.

**Bottom-Up DP**
```python
from typing import List
def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1 # One way to make 0
    
    for coin in coins:
        for amt in range(coin, amount+1):
            dp[amt] += dp[amt-coin]
    return dp[amount]
```

Dry Run (amount = 5, coins = [1, 2, 5])
init: [1, 0, 0, 0, 0, 0]

coin=1 amt=1 dp[1] += 1
coin=1 amt=2 dp[2] += dp[2-1] = dp[1] = 1
coin=1 amt=3 dp[3] += dp[3-1] = dp[2] = 1
coin=1 amt=4 dp[4] += dp[4-1] = dp[3] = 1
coin=1 amt=5 dp[5] += dp[5-1] = dp[4] = 1
dp = [1, 1, 1, 1, 1, 1]

coin=2 amt=2 dp[2] += dp[2-2] = 2
coin=2 amt=3 dp[3] += dp[3-2] = 2
coin=2 amt=4 dp[4] += dp[4-2] = dp[2] = 3
coin=2 amt=5 dp[5] += dp[5-2] = dp[3] = 3
dp = [1, 1, 2, 2, 3, 3]

coin=5 amt=5 dp[5] += dp[5-5] = 1
dp = [1, 1, 2, 2, 3, 4]

TC: O(amount x len(coins))
SC: O(amount)

**Brute Force**
```python
from typing import List
def change(amount: int, coins: List[int]) -> int:
    def helper(amount, index):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        
        total = 0
        for i in range(index, len(coins)):
            total += helper(amount-coins[i], i)
        return total
    return helper(amount, 0)
```

**Top-Down with Memoization**
```python
from typing import List
def change(amount: int, coins: List[int]) -> int:
    memo = {}
    def helper(amount, index):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if (amount, index) in memo:
            return memo[(amount, index)]
        
        total = 0
        for i in range(index, len(coins)):
            total += helper(amount-coins[i], i)
        memo[(amount, index)] = total
        return total
    return helper(amount, 0)
```

# Inverse Coin Change
**Problem:** Given numWays where numWays[i] is the number of ways to form
amount i+1 using some unknown coin set, recover the coins. Return [] if no
valid set exists.

**Example:** numWays = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5] (1-indexed)
- Amount 1: 0 ways -> no coin 1
- Amount 2: 1 way -> coin 2 exists [2]
- Amount 3: 0 ways -> no coin 3
- Amount 4: 2 ways -> 4 and 2+2, so 4 exists [2, 4]
- Amount 5: 0 ways -> no coin 5
- Amount 6: 3 ways -> 6, 4+2, 2+2+2, so coin 6 exists [2, 4, 6]
- Can continue until number 10

Answer: [2, 4, 6]

Walk through amounts 1..n in order. For each amount index:
    
1. Compute currentNumWays = ways to form index with coins built so far.
    
2. Compare to numWays[index-1]:
    - Equal -> index is not a coin, skip
    - Off by exactly 1 -> index itself must be a coin (adding it gives
   exactly one new combination: index alone)
    - Otherwise -> impossible, return []

Why off by exactly 1?

If index is a coin, the only new combination it introduces at amount index
is [index] itself (any combo using index more than once would need a larger
amount). All other combinations already existed with smaller coins.

**Solution with Memoization**

```python
from typing import List
class Solution:
    def helper(self, coins, amount, index, memo):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if (amount, index) in memo:
            return memo[(amount, index)]
        
        total = 0
        for i in range(index, len(coins)):
            total += self.helper(coins, amount-coins[i], i, memo)
        
        memo[(amount, index)] = total
        
        return total
    
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        coins = []
        memo = {}

        for index in range(1, n+1):
            expected = numWays[index-1]
            current = self.helper(coins, index, 0, memo)
            
            if current == expected:
                continue
            elif expected == current + 1:
                coins.append(index)
                memo = {} # coin set changed -> invalidate memo
            else:
                return []

        return coins
```

Memo Invalidation: Every time we append a coin, the coin set changes, so
any previously cached helper(amount, index) is stale. Reset memo = {} whenever
we add a coin.

Time Complexity: O(n^2 x k) where k = number of coins discovered. For each
amount we recompute combinations; memo amortizes within one amount's expansion.

Space Complexity: O(n) for memo + coins.

Memo Key: The memo key is whatever parameters fully identify the subproblem (i.e., the ones
that change across recursive calls).

**The rule**

A subproblem is uniquely determined by the state of recursion. The memo
key must include every parameter that varies AND affects the answer.

- Variables that change but don't affect the answer → don't include them.
- Variables that affect the answer but never change → don't include them (they're constants in this
  context).
- Variables that change AND affect the answer → must include.