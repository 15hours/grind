package main

func uniquePathsBFApproach(m int, n int) int {
	var traverse func(i, j int) int
	traverse = func(i, j int) int {
		if i >= m || j >= n {
			return 0
		}
		if i == m-1 && j == n-1 {
			return 1
		}

		return traverse(i+1, j) + traverse(i, j+1)
	}

	return traverse(0, 0)
}

func uniquePathsTopDownApproach(m int, n int) int {
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[0][0] = 1

	var traverse func(i, j int) int
	traverse = func(i, j int) int {
		if i < 0 || j < 0 {
			return 0
		}
		if dp[i][j] != 0 {
			return dp[i][j]
		}

		dp[i][j] = traverse(i-1, j) + traverse(i, j-1)
		return dp[i][j]
	}

	return traverse(m-1, n-1)
}

func uniquePathsBottomUpApproach(m int, n int) int {
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

    for i := 0; i < m; i++ {
        dp[i][0] = 1
    }
    for j := 0; j < n; j++ {
        dp[0][j] = 1
    }

    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        }
    }

	return dp[m-1][n-1]
}
