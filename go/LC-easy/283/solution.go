package main

import (
	"fmt"
)

func BFApproach(nums []int) []int {
	var countZeroes int

	for _, num := range nums {
		if num == 0 {
			countZeroes++
		}
	}

	for i := 0; i < countZeroes; i++ {
		for j := 0; j < len(nums)-i-1; j++ {
			if nums[j] == 0 {
				tmp := nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = tmp
			}
		}
	}

	return nums
}

func snowballApproach(nums []int) []int {
	var snowballSize int

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			snowballSize++
		} else {
			tmp := nums[i]
			nums[i] = 0
			nums[i-snowballSize] = tmp
		}
	}

	return nums
}

func modifiedSnowballApproach(nums []int) []int {
	var nonZeroIndex int

	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[nonZeroIndex] = nums[nonZeroIndex], nums[i]
			nonZeroIndex++
		}
	}

	return nums
}

func twoPointersApproach(nums []int) []int {
	var l int

	for r := 0; r < len(nums); r++ {
		if nums[r] != 0 {
			nums[l] = nums[r]
			l++
		}
	}

	for ; l < len(nums); l++ {
		nums[l] = 0
	}

	return nums
}

func main() {
	fmt.Println(snowballApproach([]int{1, 2, 3, 0, 0}))
	fmt.Println("hello")
}
