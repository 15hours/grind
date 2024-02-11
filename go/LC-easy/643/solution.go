package main

import "math"

func findMaxAverage(nums []int, k int) float64 {
	var maxSum int = math.MinInt
	var tmpSum int

	for i := 0; i < len(nums); i++ {
		if i < k {
			tmpSum += nums[i]
		} else {
			if tmpSum > maxSum {
				maxSum = tmpSum
			}
			tmpSum += nums[i] - nums[i-k]
		}
	}

    if tmpSum > maxSum {
        maxSum = tmpSum
    }

	return float64(maxSum) / float64(k)
}
