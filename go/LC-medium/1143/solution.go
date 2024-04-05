package main

func longestCommonSubsequenceBottomUpApproach(text1 string, text2 string) int {
	m := len(text1)
	n := len(text2)
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	if text1[0] == text2[0] {
		dp[0][0] = 1
	}

	for i := 1; i < m; i++ {
		if text1[i] == text2[0] {
			dp[i][0] = 1
		} else {
			dp[i][0] = max(dp[i-1][0], 0)
		}
	}

	for i := 1; i < n; i++ {
		if text1[0] == text2[i] {
			dp[0][i] = 1
		} else {
			dp[0][i] = max(dp[0][i-1], 0)
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if text1[i] == text2[j] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}

	return dp[m-1][n-1]
}

func longestCommonSubsequenceTopDownApproach(text1 string, text2 string) int {
	m := len(text1)
	n := len(text2)
    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
        for j := range dp[i] {
            dp[i][j] = -1
        }
    }

	if text1[0] == text2[0] {
		dp[0][0] = 1
	}

	for i := 1; i < m; i++ {
		if text1[i] == text2[0] {
			dp[i][0] = 1
		} else {
			dp[i][0] = max(dp[i-1][0], 0)
		}

	}
    for i := 1; i < n; i++ {
        if text1[0] == text2[i] {
            dp[0][i] = 1
        } else {
            dp[0][i] = max(dp[0][i-1], 0)
        }
    }

	var traverse func(i, j int) int
	traverse = func(i, j int) int {
        if i < 0 || j < 0 {
            return 0
        }

        if dp[i][j] >= 0 {
            return dp[i][j]
        }

        if text1[i] == text2[j] {
            dp[i][j] = traverse(i - 1, j - 1) + 1
        } else {
            dp[i][j] = max(traverse(i - 1, j), traverse(i, j - 1))
        }

        return dp[i][j]
	}

	return traverse(m-1, n-1)
}
