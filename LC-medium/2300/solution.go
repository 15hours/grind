package main

import (
	"fmt"
	"sort"
)

func successfulPairs(spells []int, potions []int, success int64) []int {
	sort.Slice(potions, func(i, j int) bool {
		return potions[i] < potions[j]
	})

	pairs := []int{}
	for _, spell := range spells {
		numPairs := searchPairs(potions, spell, int(success))
		pairs = append(pairs, numPairs)
	}

	return pairs
}

func searchPairs(list []int, a, c int) int {
	n := len(list)
	left, right := 0, n-1

	for left <= right {
		mid := left + (right-left)/2
		if a*list[mid] < c {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return n - left
}

func main() {
	spells := []int{5, 1, 3}
	potions := []int{4, 5, 2, 1, 3}
	fmt.Println(successfulPairs(spells, potions, 7))
}
