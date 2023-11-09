class Solution:

    def bf_approach(self, n: int) -> int:
        print("[Brute force (TLE)]")
        print("space complexity: O(n)")
        print("time complexity: O(2^n)")

        def recursion(x: int) -> int:
            if x > n:
                return 0
            if x == n:
                return 1
            return recursion(x + 1) + recursion(x + 2)

        return recursion(0)

    def dp_top_down_approach(self, n: int) -> int:
        print("[DP top down]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        memo = [0] * n

        def recursion(x: int) -> int:
            if x > n:
                return 0
            if x == n:
                return 1
            if memo[x] > 0:
                return memo[x]

            memo[x] = recursion(x + 1) + recursion(x + 2)

            return memo[x]

        return recursion(0)

    def dp_bottom_up_approach(self, n: int) -> int:
        print("[DP bottom up]")
        print("space complexity: O(n)")
        print("time complexity: O(n)")

        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for x in range(3, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]

        return dp[n]

    def fibbonaci_number_approach(self, n: int) -> int:
        print("[Fibbonaci number]")
        print("space complexity: O(1)")
        print("time complexity: O(n)")

        if n <= 2:
            return n

        F_prev = 1
        F_curr = 2
        for x in range(3, n + 1):
            F_curr, F_prev = F_prev + F_curr, F_curr

        return F_curr
