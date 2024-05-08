package main

func largestAltitude(gain []int) int {
	currentAltitude := 0
	maxAltitude := 0

	for _, num := range gain {
		currentAltitude += num
		if currentAltitude > maxAltitude {
			maxAltitude = currentAltitude
		}
	}

	return maxAltitude
}
