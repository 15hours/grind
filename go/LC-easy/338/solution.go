package main

import (
	"fmt"
	"math"
)

func countBits1(n int) []int {
	result := make([]int, n+1)

	for i := 0; i < n+1; i++ {
		countOnes := 0
		currNum := i
		for currNum != 0 {
			if currNum%2 != 0 {
				countOnes++
			}
			currNum /= 2
		}

		result[i] = countOnes
	}

	return result
}

func countBits2(n int) []int {
	result := make([]int, n+1)
	degree := 0

	for i := 1; i < n+1; i++ {
		if i == int(math.Pow(2, float64(degree+1))) {
			degree++
		}

		result[i] = 1 + result[i-int(math.Pow(2, float64(degree)))]
	}

	return result
}

func countBits3(n int) []int {
	result := make([]int, n+1)

	for i := 0; i <= n; i++ {
		result[i] = result[i>>1] + i%2
	}

	return result
}

func main() {
	fmt.Println(countBits1(5))
	fmt.Println(countBits2(5))
	fmt.Println(countBits3(5))
}
