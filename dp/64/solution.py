class Solution:

    def bf_approach(self, grid: list[list[int]]) -> int:
        print("[Brute force (TLE)]")
        pritn("space complexity: O(m + n)")
        print("time complexity: O(2^(m+n))")

        num_rows, num_cols = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            path_cost = 0

            if i + 1 >= num_rows and j + 1 < num_cols:
                path_cost = dfs(i, j + 1)
            elif j + 1 >= num_cols and i + 1 < num_rows:
                path_cost = dfs(i + 1, j)
            elif i + 1 < num_rows and j + 1 < num_cols:
                path_cost = min(dfs(i + 1, j), dfs(i, j + 1))

            return grid[i][j] + path_cost

        return dfs(0, 0)

    def dp_top_down_approach(self, grid: list[list[int]]) -> int:
        print("[DP top down - memoization]")
        print("space complexity: O(m * n)")
        print("time complexity: O(m * n)")

        num_rows, num_cols = len(grid), len(grid[0])
        dp = [[0] * num_cols for _ in range(num_rows)]
        
        def dfs(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return grid[i][j]

            if i < 0 or j < 0:
                return float('inf')
            if dp[i][j] > 0:
                return dp[i][j]

            dp[i][j] = grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))
            return dp[i][j]

        return dfs(num_rows - 1, num_cols - 1)

    def dp_bottom_up_approach(self, grid: list[list[int]]) -> int:
        print("[DP bottom up - tabulation]")
        print("space complexity: O(m * n)")
        print("time complexity: O(m * n)")

        num_rows, num_cols = len(grid), len(grid[0])
        dp = [[0] * num_cols for _ in range(num_rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, num_rows):
            dp[i][0] = grid[i][0] + dp[i - 1][0]

        for j in range(1, num_cols):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        
        for i in range(1, num_rows):
            for j in range(1, num_cols):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[num_rows - 1][num_cols - 1]
