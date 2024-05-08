package main

import "slices"

func condition(v int, piles []int) int {
	hResult := 0
	for _, p := range piles {
		hResult += (p-1)/v + 1
	}
	return hResult
}

// time O(n log(m)), where m = max(piles)
func minEatingSpeed(piles []int, h int) int {
	l, r := 1, slices.Max(piles)

	for l < r {
		mid := l + (r-l)/2
		if condition(mid, piles) > h {
			l = mid + 1
		} else {
			r = mid
		}
	}

	return l
}
