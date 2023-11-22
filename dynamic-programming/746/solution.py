class Solution:

    def bf_approach(self, cost: list[int]) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(n)")
        print("time complexity: O(2^n)")

        n = len(cost)

        def dfs(i: int) -> int:
            if i < 0:
                return 0

            return cost[i] + min(dfs(i - 1), dfs(i - 2))

        return min(dfs(n - 1), dfs(n - 2))

    def dp_top_down_approach(self, cost: list[int]) -> int:
        print("[DP top down - memoization]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        n = len(cost)
        dp = [0] * n

        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if dp[i] > 0:
                return dp[i]

            dp[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
            return dp[i]

        return min(dfs(n - 1), dfs(n - 2))

    def dp_bottom_up_approach(self, cost: list[int]) -> int:
        print("[DP bottom up - tabulation]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])

    def dp_bottom_up_const_approach(self, cost: list[int]) -> int:
        print("[DP bottom up - const space]")
        print("space complexity: O(1)")
        print("time complexity: O(n)")

        n = len(cost)
        down_two = cost[0]
        down_one = cost[1]

        for i in range(2, n):
            tmp = down_one
            down_one = cost[i] + min(down_one, down_two)
            down_two = tmp

        return min(down_one, down_two)
