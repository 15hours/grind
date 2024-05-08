package main

import "fmt"

func checkStraightLine(coordinates [][]int) bool {
	x0, y0 := coordinates[0][0], coordinates[0][1]
	x1, y1 := coordinates[1][0], coordinates[1][1]

	for i := 2; i < len(coordinates); i++ {
		x, y := coordinates[i][0], coordinates[i][1]

		if (x1-x0)*(y-y1) != (y1-y0)*(x-x1) {
			return false
		}
	}

	return true
}

func main() {
	coordinates1 := [][]int{
		{1, 2},
		{2, 3},
		{3, 4},
		{4, 5},
		{5, 6},
		{6, 7},
	}
	fmt.Println(checkStraightLine(coordinates1))

	coordinates2 := [][]int{
		{1, 1},
		{2, 2},
		{3, 4},
		{4, 5},
		{5, 6},
		{7, 7},
	}
	fmt.Println(checkStraightLine(coordinates2))

	coordinates3 := [][]int{
		{0, 0},
		{0, 1},
		{0, -1},
	}
	fmt.Println(checkStraightLine(coordinates3))
}
