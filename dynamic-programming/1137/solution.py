class Solution:

    def formula_approach(self, n: int) -> int:
        print("[formula]")
        print("[space complexity: O(1)]")
        print("[time complexity: O(n)]")

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        T_prev_prev = 0
        T_prev = 1
        T_cur = 1
        for x in range(3, n + 1):
            tmp = T_cur
            T_cur = T_prev_prev + T_prev + T_cur
            T_prev, T_prev_prev = tmp, T_prev

        return T_cur

    def dp_top_down_approach(self, n: int) -> int:
        print("[DP top down]")
        print("[space complexity: O(n)]")
        print("[time complexity: O(n)]")

        memo = [0] * (n + 1)

        def recursion(x: int) -> int:
            if x < 1:
                return 0
            if x == 1:
                return 1
            if memo[x] > 0:
                return memo[x]

            memo[x] = recursion(x - 1) + recursion(x - 2) + recursion(x - 3)
            return memo[x]

        return recursion(n)

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

        for x in range(3, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2] + dp[x - 3]

        return dp[n]
