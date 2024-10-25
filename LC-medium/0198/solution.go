package main

import "fmt"

func robBFApproach(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}

	var traverse func(node int) int
	traverse = func(node int) int {
		if node > n-1 {
			return 0
		}

		return max(traverse(node+1), nums[node]+traverse(node+2))
	}

	return max(traverse(0), traverse(1))
}

func tobBottomUpApproach(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	dp := make([]int, n)

	dp[0] = nums[0]
	dp[1] = nums[1]
	for i := 2; i < n; i++ {
		dp[i] = max(dp[i-1], nums[i]+dp[i-2])
	}

	return max(dp[n-1], dp[n-2])
}

func robTopDownApproach(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}

	dp := make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = -1
	}

	var traverse func(node int) int
	traverse = func(node int) int {
		if node < 0 {
			return 0
		}
		if dp[node] != -1 {
			return dp[node]
		}

		dp[node] = max(traverse(node-1), nums[node]+traverse(node-2))

		return dp[node]
	}

	return traverse(n - 1)
}

func robBottomUpConstSpaceApproach(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}

	prevPrev := nums[0]
	prev := max(nums[0], nums[1])
	curr := 0
	for i := 2; i < n; i++ {
		curr = max(prev, nums[i]+prevPrev)
		prev, prevPrev = curr, prev
	}

	return max(curr, prev)
}

func main() {
	fmt.Println(robBFApproach([]int{1, 2, 3, 1}))
	fmt.Println(robBFApproach([]int{2, 7, 9, 3, 1}))
	fmt.Println(robTopDownApproach([]int{1, 2, 3, 1}))
	fmt.Println(robTopDownApproach([]int{2, 7, 9, 3, 1}))
}
