package main

import "fmt"

func longestOnes(nums []int, k int) int {
	var l, r, currZeroes, result int
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			currZeroes++
		}
		for currZeroes > k {
			if nums[l] == 0 {
				currZeroes--
			}
			l++
		}
		r++
		result = max(result, r-l)
	}

	return result
}

func main() {
	fmt.Println(longestOnes([]int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}, 2))
	fmt.Println(longestOnes([]int{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1}, 3))
}
