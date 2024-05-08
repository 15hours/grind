package main

import "fmt"

func setDifference(a, b []int) []int {
	setB := make(map[int]bool)
	diffAB := []int{}

	for _, num := range b {
		setB[num] = true
	}

	for _, num := range a {
		if _, exists := setB[num]; !exists {
			diffAB = append(diffAB, num)
			setB[num] = true
		}
	}

	return diffAB
}

func findDifference(nums1 []int, nums2 []int) [][]int {
	return [][]int{setDifference(nums1, nums2), setDifference(nums2, nums1)}
}

func main() {
	fmt.Println(findDifference([]int{1, 2, 3}, []int{2, 4, 6}))
}
