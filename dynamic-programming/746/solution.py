class Solution:

    def bf_approach(self, cost: list[int]) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(1)")
        print("time complexity: O(2^n)")

        num_stairs = len(cost)

        def recursion(x: int) -> int:
            if x == 0 or x == 1:
                return cost[x]

            if x != num_stairs:
                return cost[x] + min(recursion(x - 1), recursion(x - 2))
            else:
                return min(recursion(x - 1), recursion(x - 2))

        return recursion(num_stairs)

    def dp_bottom_up_approach(self, cost: list[int]) -> int:
        print("[DP bottom up]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        num_stairs = len(cost)
        dp = [float('inf')] * num_stairs
        dp[0] = cost[0]
        dp[1] = cost[1]

        for stair in range(2, num_stairs):
            dp[stair] = cost[stair] + min(dp[stair - 1], dp[stair - 2])

        return min(dp[num_stairs - 1], dp[num_stairs - 2])

    def dp_top_down_approach(self, cost: list[int]) -> int:
        print("[DP top down]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        num_stairs = len(cost)
        memo = [float('inf')] * (num_stairs + 1)

        def recursion(x: int) -> int:
            if x == 0 or x == 1:
                return cost[x]
            if memo[x] < float('inf'):
                return memo[x]

            if x != num_stairs:
                memo[x] = cost[x] + min(recursion(x - 1), recursion(x - 2))
            else:
                memo[x] = min(recursion(x - 1), recursion(x - 2))

            return memo[x]

        return recursion(num_stairs)
