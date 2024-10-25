package main

import "fmt"

func maxAreaBFApproach(height []int) int {
	n := len(height)
	s := 0
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			a := min(height[i], height[j])
			b := j - i
			tmpS := a * b
			if tmpS > s {
				s = tmpS
			}
		}
	}

	return s
}

func maxAreaPointersApproach(height []int) int {
	n := len(height)
	l, r := 0, n-1
	s := min(height[l], height[r]) * (r - l)

	for l < r {
		if height[l] < height[r] {
			l++
		} else {
			r--
		}

		tmpS := min(height[l], height[r]) * (r - l)
		if tmpS > s {
			s = tmpS
		}
	}

	return s
}

func main() {
	fmt.Println(maxAreaBFApproach([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
	fmt.Println(maxAreaPointersApproach([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
}
