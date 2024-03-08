package main

func uniqueOccurrences(arr []int) bool {
	count := make(map[int]int)
	for _, num := range arr {
		count[num]++
	}

	setOfValues := make(map[int]int)
	for _, value := range count {
		setOfValues[value]++
		if setOfValues[value] != 1 {
			return false
		}
	}

	return true
}
