package main

import (
	"fmt"
	"slices"
)

func singleNumberUsingMap(nums []int) int {
	count := make(map[int]int)

	for _, num := range nums {
		count[num]++
	}

	for key, value := range count {
		if value == 1 {
			return key
		}
	}

	return -1
}

func singleNumberUsingSorting(nums []int) int {
	sortedArr := make([]int, len(nums))
	copy(sortedArr, nums)
	slices.Sort(sortedArr)

	for i := 1; i < len(sortedArr); i = i + 2 {
		if sortedArr[i] != sortedArr[i-1] {
			return sortedArr[i-1]
		}
	}

	return sortedArr[len(sortedArr)-1]
}

func singleNumberUsingXOR(nums []int) int {
	xorResult := 0

    for _, num := range nums {
		xorResult ^= num
	}

	return xorResult
}

func main() {
	fmt.Println(singleNumberUsingMap([]int{4, 1, 2, 1, 2}))
	fmt.Println(singleNumberUsingSorting([]int{4, 1, 2, 1, 2}))
	fmt.Println(singleNumberUsingXOR([]int{4, 1, 2, 1, 2}))
}
