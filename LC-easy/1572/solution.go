package main

import "fmt"

func diagonalSum(mat [][]int) int {
	n := len(mat)
	var result int

	for i := 0; i < n; i++ {
		result += mat[i][i]
		result += mat[i][n-i-1]
	}

	if n%2 == 1 {
		result -= mat[n/2][n/2]
	}

	return result
}

func main() {
	mat := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	fmt.Println(diagonalSum(mat))
}
