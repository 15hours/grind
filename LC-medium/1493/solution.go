package main

import "fmt"

func longestSubarray(nums []int) int {
	var l, r, currZeroes, result int

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			currZeroes++
		}

		if currZeroes > 1 {
			if nums[l] == 0 {
				currZeroes--
			}
			l++
		}

		r++
		result = max(result, r-l-1)
	}

	return result
}

func main() {
	fmt.Println(longestSubarray([]int{0, 1, 1, 1, 0, 1, 1, 0, 1}))
}
