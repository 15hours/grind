class Solution:

    def bf_approach(self, m: int, n: int) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(m + n)")
        print("time complexity: O(2^(m + n))")

        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1

            return dfs(i - 1, j) + dfs(i, j - 1)

        return dfs(m - 1, n - 1)

    def dp_top_down_approach(self, m: int, n: int) -> int:
        print("[DP top down - memoization]")
        print("space complexity: O(m*n)")
        print("time complexity:O(m*n)")

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1

        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]

            dp[i][j] = dfs(i - 1, j) + dfs(i, j - 1)
            return dp[i][j]

        return dfs(m - 1, n - 1)

    def dp_bottom_up_approach(self, m: int, n: int) -> int:
        print("[DP bottom up - tabulation]")
        print("space complexity: O(m*n)")
        print("time complexity:O(m*n)")

        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]

    def dp_bottom_up_const_approach(self, m: int, n: int) -> int:
        print("[DP bottom up - const space]")
        print("space complexity: O(min(m, n))")
        print("time complexity:O(m*n)")

        if m > n:
            m, n = n, m

        buff_arr = [1] * m

        for i in range(1, n):
            for j in range(1, m):
                buff_arr[j] += buff_arr[j - 1]

        return buff_arr[m - 1]
