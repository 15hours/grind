class Solution:

    def bf_approach(self, nums: list[int]) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(n)")
        print("time complexity: O(2^n)")

        n = max(nums)
        cost = [0] * (n + 1)
        for num in nums:
            cost[num] += num

        def dfs(i: int) -> int:
            if i < 0:
                return 0

            return max(cost[i] + dfs(i - 2), dfs(i - 1))

        return dfs(n)

    def dp_top_down_approach(self, nums: list[int]) -> int:
        print("[DP top down - memoization]")
        print("space complexity: O(k + n)")
        print("time complexity: O(k + n)")

        n = max(nums)
        cost = [0] * (n + 1)
        for num in nums:
            cost[num] += num

        dp = [float('-inf')] * (n + 1)

        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if dp[i] >= 0:
                return dp[i]

            dp[i] = max(cost[i] + dfs(i - 2), dfs(i - 1))
            return dp[i]

        return dfs(n)

    def dp_bottom_up_approach(self, nums: list[int]) -> int:
        print("[DP bottom up - tabulation]")
        print("space complexity: O(k + n)")
        print("time complexity: O(k + n)")

        n = max(nums)
        cost = [0] * (n + 1)
        for num in nums:
            cost[num] += num

        if n == 0:
            return cost[0]

        dp = [0] * (n + 1)
        dp[0] = cost[0]
        dp[1] = max(cost[0], cost[1])
        for i in range(2, n + 1):
            dp[i] = max(cost[i] + dp[i - 2], dp[i - 1])

        return dp[n]

    def dp_bottom_up_const_approach(self, nums: list[int]) -> int:
        print("[DP bottom up - const space")
        print("space complexity: O(n)")
        print("time complexity: O(k + n)")

        n = max(nums)
        cost = [0] * (n + 1)
        for num in nums:
            cost[num] += num

        if n == 0:
            return cost[0]

        prev_prev_cost = cost[0]
        prev_cost = max(cost[0], cost[1])
        cur_cost = prev_cost
        for i in range(2, n + 1):
            cur_cost = max(cost[i] + prev_prev_cost, prev_cost)
            prev_prev_cost, prev_cost = prev_cost, cur_cost

        return cur_cost
