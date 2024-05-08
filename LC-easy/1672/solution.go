package main

import "fmt"

func maximumWealth(accounts [][]int) int {
	maxSum := 0

	for _, account := range accounts {
		tmpSum := 0
		for _, money := range account {
			tmpSum += money
		}
		if tmpSum > maxSum {
			maxSum = tmpSum
		}
	}

	return maxSum
}

func main() {
	accounts := [][]int{
		{2, 8, 7},
		{7, 1, 3},
		{1, 9, 5},
	}
	fmt.Println(maximumWealth(accounts))
}
