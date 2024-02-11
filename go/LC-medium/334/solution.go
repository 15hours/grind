package main

import (
	"math"
	"slices"
)

func increasingTripletBFApproach(nums []int) bool {
	if slices.Max(nums)-slices.Min(nums) < 2 {
		return false
	}
	n := len(nums)
	for i := 0; i < n-2; i++ {

		for j := i + 1; j < n-1; j++ {
			if nums[j] <= nums[i] {
				continue
			}

			for k := j + 1; k < n; k++ {
				if nums[k] <= nums[j] {
					continue
				}
				if nums[i] < nums[j] && nums[j] < nums[k] {
					return true
				}
			}
		}
	}

	return false
}

func increasingTriplet(nums []int) bool {
	firstNum, secondNum := math.MaxInt, math.MaxInt

	for _, num := range nums {
		if num <= firstNum {
			firstNum = num
		} else if num <= secondNum {
			secondNum = num
		} else {
			return true
		}
	}

	return false
}
