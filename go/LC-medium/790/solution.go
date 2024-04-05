package main

func numTilingsDPBottomUpApproach(n int) int {
	if n <= 2 {
		return n
	}

	mod := 1e9 + 7
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2

	for i := 3; i <= n; i++ {
		dp[i] = 2*dp[i-1] + dp[i-3]
		dp[i] %= int(mod)
	}

	return dp[n]
}

func numTilingsDPTopDownApproach(n int) int {
	if n <= 2 {
		return n
	}

	mod := 1e9 + 7
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2

	var traverse func(i int) int
	traverse = func(i int) int {
		if i < 0 {
			return 0
		}
		if dp[i] > 0 {
			return dp[i]
		}

		dp[i-1] = traverse(i-1) % int(mod)
		return (2*dp[i-1] + dp[i-3]) % int(mod)
	}

	return traverse(n)
}
