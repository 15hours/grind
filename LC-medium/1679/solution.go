package main

import (
	"fmt"
	"slices"
)

// time O(n^2)
// space O(n)
func maxOperationsBFApproach(nums []int, k int) int {
	n := len(nums)
	count := 0
	removed := make([]bool, n)

	for i := 0; i < n-1; i++ {
		if removed[i] {
			continue
		}

		for j := i + 1; j < n; j++ {
			if removed[j] {
				continue
			}
			if nums[i]+nums[j] == k {
				count++
				removed[i] = true
				removed[j] = true
				break
			}
		}
	}

	return count
}

// time O(nlogn)
// spice O(n)
func maxOperationsSortApproach(nums []int, k int) int {
	n := len(nums)
	sortedNums := make([]int, n)
	copy(sortedNums, nums)
	slices.Sort(sortedNums)

	counter := 0
	l, r := 0, n-1
	for l < r {
		curSum := sortedNums[l] + sortedNums[r]
		if curSum == k {
			counter++
			l++
			r--
		} else if curSum > k {
			r--
		} else {
			l++
		}
	}

	return counter
}

func maxOperationsMapApproach(nums []int, k int) int {
	numsMap := make(map[int]int)

	counter := 0
	for _, num := range nums {
		target := k - num
		if value, exists := numsMap[target]; exists && value > 0 {
			counter++
			numsMap[target] = value - 1
		} else {
			numsMap[num]++
		}
	}

	return counter

}

func main() {
	fmt.Println(maxOperationsBFApproach([]int{3, 1, 3, 4, 3}, 6))
	fmt.Println(maxOperationsBFApproach([]int{1, 2, 3, 4}, 5))
	fmt.Println(maxOperationsSortApproach([]int{3, 1, 3, 4, 3}, 6))
	fmt.Println(maxOperationsSortApproach([]int{1, 2, 3, 4}, 5))
	fmt.Println(maxOperationsMapApproach([]int{3, 1, 3, 4, 3}, 6))
	fmt.Println(maxOperationsMapApproach([]int{1, 2, 3, 4}, 5))
}
