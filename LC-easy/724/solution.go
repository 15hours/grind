package main

func pivotIndex(nums []int) int {
	sumLeft, sumRight := 0, 0

	for _, num := range nums {
		sumRight += num
	}

	for i := 0; i < len(nums); i++ {
		sumRight -= nums[i]

		if sumLeft == sumRight {
			return i
		}

		sumLeft += nums[i-1]
	}

	return -1
}
