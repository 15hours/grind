class Solution:

    def bf_approach(self, n: int) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(n)")
        print("time complexity: O(2^n)")

        def dfs(i: int) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)

    def dp_top_down_approach(self, n: int) -> int:
        print("[DP top down]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        dp = [0] * n

        def dfs(i: int) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            if dp[i] > 0:
                return dp[i]

            dp[i] = dfs(i + 1) + dfs(i + 2)

            return dp[i]

        return dfs(0)

    def dp_bottom_up_approach(self, n: int) -> int:
        print("[DP bottom up]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def dp_bottom_up_const_approach(self, n: int) -> int:
        print("[DP bottom up const space]")
        print("space complexity: O(1)")
        print("time complexity: O(n)")

        if n <= 2:
            return n

        F_prev = 1
        F_curr = 2
        for _ in range(3, n + 1):
            F_curr, F_prev = F_prev + F_curr, F_curr

        return F_curr
