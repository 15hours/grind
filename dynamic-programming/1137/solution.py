class Solution:

    def bf_approach(self, n: int) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(n)")
        print("time complexity: O(3^n)")

        def dfs(i: int) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            return dfs(i - 1) + dfs(i + 2) - dfs(i - 3)

        return dfs(n)

    def dp_top_down_approach(self, n: int) -> int:
        print("[DP top down]")
        print("[space complexity: O(n)]")
        print("[time complexity: O(n)]")

        dp = [0] * (n + 1)

        def dfs(i: int):
            if i < 1:
                return 0
            if i == 1:
                return 1
            if dp[i] > 0:
                return dp[i]

            dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            return dp[i]

        return dfs(n)

    def dp_bottom_up_approach(self, n: int) -> int:
        print("[DP bottom up]")
        print("[space complexity: O(n)]")
        print("[time complexity: O(n)]")

        if n < 2:
            return n
        if n == 2:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]

    def dp_bottom_up_const_approach(self, n: int) -> int:
        print("[DP bottom up with constant space]")
        print("[space complexity: O(1)]")
        print("[time complexity: O(n)]")

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        T_prev_prev = 0
        T_prev = 1
        T_cur = 1
        for _ in range(3, n + 1):
            tmp = T_cur
            T_cur = T_prev_prev + T_prev + T_cur
            T_prev, T_prev_prev = tmp, T_prev

        return T_cur
