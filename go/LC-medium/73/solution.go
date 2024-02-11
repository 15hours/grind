package main

import "fmt"

func setZeroes(matrix [][]int) {
	numRows := len(matrix)
	numCols := len(matrix[0])

	zeroElements := [][]int{}

	for i := 0; i < numRows; i++ {
		for j := 0; j < numCols; j++ {
			if matrix[i][j] == 0 {
				zeroElements = append(zeroElements, []int{i, j})
			}
		}
	}

	for _, zeroElement := range zeroElements {
		iTarget, jTarget := zeroElement[0], zeroElement[1]

		for i := 0; i < numRows; i++ {
			matrix[i][jTarget] = 0
		}
		for j := 0; j < numCols; j++ {
			matrix[iTarget][j] = 0
		}
	}

	fmt.Println(matrix)
}

func setZeroesZeroSpaceApproach(matrix [][]int) {
	numRows := len(matrix)
	numCols := len(matrix[0])

	zeroRow, zeroCol := false, false
	for i := 0; i < numRows; i++ {
		if matrix[i][0] == 0 {
			zeroCol = true
		}
	}
	for j := 0; j < numCols; j++ {
		if matrix[0][j] == 0 {
			zeroRow = true
		}
	}

	for i := 1; i < numRows; i++ {
		for j := 1; j < numCols; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	for i := 1; i < numRows; i++ {
		if matrix[i][0] == 0 {
			for j := 0; j < numCols; j++ {
				matrix[i][j] = 0
			}
		}
	}

	for j := 1; j < numCols; j++ {
		if matrix[0][j] == 0 {
			for i := 0; i < numRows; i++ {
				matrix[i][j] = 0
			}
		}
	}

	if zeroRow {
		for j := 0; j < numCols; j++ {
			matrix[0][j] = 0
		}
	}
	if zeroCol {
		for i := 0; i < numRows; i++ {
			matrix[i][0] = 0
		}
	}

	fmt.Println(matrix)
}

func main() {
	matrix1 := [][]int{
		{1, 1, 1},
		{1, 0, 1},
		{1, 1, 1}}
	setZeroes(matrix1)
	matrix2 := [][]int{
		{0, 1, 2, 0},
		{3, 4, 5, 2},
		{1, 3, 1, 5}}
	setZeroesZeroSpaceApproach(matrix2)
}
