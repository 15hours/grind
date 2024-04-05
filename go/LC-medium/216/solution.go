package main

import "fmt"

func backtrack(combinations *[][]int, comb []int, start int, target int, counter int) {
	if counter < 0 || target < 0 {
		return
	}
	if counter == 0 && target == 0 {
		*combinations = append(*combinations, comb)
		return
	}

	for i := start; i <= 9; i++ {
		tmpComb := make([]int, len(comb))
		copy(tmpComb, comb)
		tmpComb = append(tmpComb, i)

		backtrack(combinations, tmpComb, i+1, target-i, counter-1)
	}
}

func combinationSum3(k int, n int) [][]int {
	var combinations [][]int

	backtrack(&combinations, []int{}, 1, n, k)
	return combinations
}

func main() {
	fmt.Println(combinationSum3(4, 24))
}
