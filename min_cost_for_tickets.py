from typing import List

"""
Time Complexity: O(3^D), where D is the total number of days in the year (or
specifically the range up to the last travel day). At each day, we branch into
3 recursive calls.

Space Complexity: O(D), representing the depth of the recursion stack.
"""


def mincostTickets_brute_force(days: List[int], costs: List[int]) -> int:
    # Set of days to travel for O(1) lookup
    travel_days = set(days)

    def helper(current_day: int) -> int:
        # Base Case: If we are past the last travel day, cost is 0
        if current_day > days[-1]:
            return 0

        # If not a travel day, we don't need a ticket
        if current_day not in travel_days:
            return helper(current_day + 1)

        # If it is a travel day, choose the minimum among the 3 options
        # 1-day pass: covers current day
        option1 = costs[0] + helper(current_day + 1)
        # 7-day pass: covers current day + next 6 days
        option2 = costs[1] + helper(current_day + 7)
        # 30-day pass: covers current day + next 29 days
        option3 = costs[2] + helper(current_day + 30)

        return min(option1, option2, option3)

    return helper(days[0])


def minCostTickets_memoization(days: List[int], costs: List[int]) -> int:
    memo = {}

    def helper(i: int) -> int:
        # Base case: All travel days covered
        if i >= len(days):
            return 0

        if i in memo:
            return memo[i]

        # Option 1: 1-day pass
        res = costs[0] + helper(i + 1)

        # Option 2: 7-day pass
        # Find the next travel day index that is >= days[i] + 7
        j = i
        while j < len(days) and days[j] < days[i] + 7:
            j += 1
            res = min(res, costs[1] + helper(j))

        # Option 3: 30-day pass
        # Find the next travel day index that is >= days[i] + 30
        j = i
        while j < len(days) and days[j] < days[i] + 30:
            j += 1
            res = min(res, costs[2] + helper(j))

        memo[i] = res
        return res

    return helper(0)


def minCostTickets_tabulation(days: List[int], costs: List[int]) -> int:
    travel_days = set(days)
    last_day = days[-1]
    dp = [0] * (last_day + 1)

    for day in range(1, last_day + 1):
        if day not in travel_days:
            dp[day] = dp[day - 1]
        else:
            dp[day] = min(
                dp[day - 1] + costs[0],
                dp[max(0, day - 7)] + costs[1],
                dp[max(0, day - 30)] + costs[2],
            )
    return dp[last_day]


def minCostTickets_tabulation(days: list[int], costs: list[int]) -> int:
    # Use a set for fast O(1) lookups
    travel_days = set(days)

    # dp[i] is the min cost to finish travel from day i to 365
    dp = [0] * 367

    # Iterate backwards from the last possible day
    for i in range(365, 0, -1):
        if i not in travel_days:
            dp[i] = dp[i + 1]
        else:
            # Min cost of buying 1, 7, or 30 day ticket
            dp[i] = min(
                costs[0] + dp[i + 1],
                costs[1] + dp[min(366, i + 7)],
                costs[2] + dp[min(366, i + 30)],
            )

    return dp[days[0]]


from collections import deque


def minCostTickets(days: list[int], costs: list[int]) -> int:
    # Use a queue to store (day_covered, cost) for 7-day and 30-day passes
    last7 = deque()
    last30 = deque()
    cost = 0

    for d in days:
        # 1. Clean up passes that have expired
        while last7 and last7[0][0] + 7 <= d:
            last7.popleft()
        while last30 and last30[0][0] + 30 <= d:
            last30.popleft()

        # 2. Add current day's cost to our active passes
        # The cost to be covered on day 'd' is the min of:
        # - Adding a 1-day pass to the previous total cost
        # - Using a 7-day pass (cost + current total from 7 days ago)
        # - Using a 30-day pass (cost + current total from 30 days ago)
        cost = min(
            cost + costs[0],
            (last7[0][1] if last7 else 0) + costs[1],
            (last30[0][1] if last30 else 0) + costs[2],
        )

        # 3. Add the new state to our queues
        last7.append((d, cost))
        last30.append((d, cost))

    return cost