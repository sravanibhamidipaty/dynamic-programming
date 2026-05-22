def nth_tribonacci_number_brute_force(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return nth_tribonacci_number_brute_force(n-1) + nth_tribonacci_number_brute_force(n-2) + nth_tribonacci_number_brute_force(n-3)

def nth_tribonacci_number_memoization(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    memo = {0:0, 1:1, 2:1}

    def helper(num: int) -> int:
        if num in memo:
            return memo[num]
        memo[num] = helper(num-1) + helper(num-2) + helper(num-3)
        return memo[num]
    return helper(n)

def nth_tribonacci_number_tabulation(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[n]

def nth_tribonacci_number_optimal(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    first = 0
    second = 1
    third = 1

    for _ in range(3, n+1):
        next_val = first + second + third
        first = second
        second = third
        third = next_val
    return third