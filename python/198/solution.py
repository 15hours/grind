class Solution:

    def bf_approach(self, nums: list[int]) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(n)")
        print("time complexity: O(2^n)")

        n = len(nums)

        def dfs(i: int) -> int:
            if i < 0:
                return 0

            return max(nums[i] + dfs(i - 2), dfs(i - 1))

        return dfs(n - 1)

    def dp_top_down_approach(self, nums: list[int]) -> int:
        print("[DP top down - memoization]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        n = len(nums)
        dp = [float('-inf')] * n

        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if dp[i] >= 0:
                return dp[i]

            dp[i] = max(nums[i] + dfs(i - 2), dfs(i - 1))
            return dp[i]

        return dfs(n - 1)

    def dp_bottom_up_approach(self, nums: list[int]) -> int:
        print("[DP bottom up - tabulation]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        n = len(nums)
        if n == 1:
            return nums[n - 1]

        dp = [0] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n + 1):
            if i != n:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            else:
                dp[i] = max(dp[i - 2], dp[i - 1])

        return dp[n]

    def dp_bottom_up_const_approach(self, nums: list[int]) -> int:
        print("[DP bottom up - const space]")
        print("space complexity: O(1)")
        print("time complexity: O(n)")

        n = len(nums)
        if n == 1:
            return nums[n - 1]

        prev_prev_cost = nums[0]
        prev_cost = max(nums[0], nums[1])
        cur_cost = 0
        answer = 0
        for i in range(2, n + 1):
            if i != n:
                cur_cost = max(nums[i] + prev_prev_cost, prev_cost)
            else:
                answer = max(prev_prev_cost, prev_cost)

            prev_cost, prev_prev_cost = cur_cost, prev_cost

        return answer
