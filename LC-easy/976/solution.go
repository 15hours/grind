package main

import (
	"fmt"
	"slices"
)

func largestPerimeter(nums []int) int {
	numsLength := len(nums)

	sortedNums := make([]int, numsLength)
	copy(sortedNums, nums)
	slices.Sort(sortedNums)

	for i := numsLength - 1; i >= 2; i-- {
		a, b, c := sortedNums[i-2], sortedNums[i-1], sortedNums[i]

		if c < a+b {
			return a + b + c
		}
	}

	return 0
}

func main() {
	fmt.Println(largestPerimeter([]int{1, 2, 1, 10}))
	fmt.Println(largestPerimeter([]int{2, 1, 2}))
}
