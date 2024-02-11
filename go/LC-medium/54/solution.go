package main

func spiralOrder(matrix [][]int) []int {
	numRows := len(matrix)
	numCols := len(matrix[0])
	result := make([]int, numRows*numCols)

	iBottom, iUpper := 0, len(matrix)
	jBottom, jUpper := 0, len(matrix[0])
	currentDirection := 0
	resultIdx := 0

	for iBottom <= iUpper-1 && jBottom <= jUpper-1 {
		switch currentDirection {
		case 0:
			for j := jBottom; j < jUpper; j++ {
				result[resultIdx] = matrix[iBottom][j]
				resultIdx++
			}
			iBottom++
		case 1:
			for i := iBottom; i < iUpper; i++ {
				result[resultIdx] = matrix[i][jUpper-1]
				resultIdx++
			}
			jUpper--
		case 2:
			for j := jUpper - 1; j >= jBottom; j-- {
				result[resultIdx] = matrix[iUpper-1][j]
				resultIdx++
			}
			iUpper--
		case 3:
			for i := iUpper - 1; i >= iBottom; i-- {
				result[resultIdx] = matrix[i][jBottom]
				resultIdx++
			}
			jBottom++
		}

		currentDirection = (currentDirection + 1) % 4
	}

	return result
}
