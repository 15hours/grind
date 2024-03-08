package main

func findPeakElement(nums []int) int {
	n := len(nums)
	if n == 1 {
		return 0
	} else if nums[0] > nums[1] {
		return 0
	} else if nums[n-1] > nums[n-2] {
		return n - 1
	}

	left, right := 1, n-2
	ans := -1
	for {
		mid := (left + right) / 2

		if nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1] {
			ans = mid
			break
		}
		if nums[mid] < nums[mid-1] {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return ans
}
