package main

import "fmt"

const M = 3

type Element struct {
	Coord [2]int
	Count int
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func traverse(grid [][]byte, n int) int {
	moves := []int{-1, 0, 1}

	maxCount := 0
	queue := []Element{}
	for j := 0; j < M; j++ {
		if grid[0][j] == 'W' {
			continue
		}
		currCount := 0
		if grid[0][j] == 'C' {
			currCount++
		}
		queue = append(queue, Element{Coord: [2]int{0, j}, Count: currCount})
	}

	for len(queue) != 0 {
		possibleMoves := queue
		queue = []Element{}

		for len(possibleMoves) != 0 {
			elem := possibleMoves[0]
			possibleMoves = possibleMoves[1:]

			currCount := elem.Count
			currI, currJ := elem.Coord[0], elem.Coord[1]
			maxCount = max(maxCount, currCount)

			for _, shiftJ := range moves {
				nextI, nextJ := currI+1, currJ+shiftJ
				if !(0 <= nextI && nextI < n && 0 <= nextJ && nextJ < 3) || grid[nextI][nextJ] == 'W' {
					continue
				}

				newCount := currCount
				if grid[nextI][nextJ] == 'C' {
					newCount++
				}

				queue = append(queue, Element{Coord: [2]int{nextI, nextJ}, Count: newCount})
			}
		}
	}

	return maxCount
}

func main() {
	var n int
	fmt.Scanf("%d", &n)

	grid := make([][]byte, n)
	for i := 0; i < n; i++ {
		var s string
		fmt.Scanf("%s", &s)

		grid[i] = make([]byte, M)
		for j := 0; j < M; j++ {
			grid[i][j] = s[j]
		}
	}

	fmt.Println(traverse(grid, n))
}
