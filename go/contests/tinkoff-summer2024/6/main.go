package main

import (
	"container/heap"
	"fmt"
	"math"
)

type Role byte

const (
	Knight Role = 'K'
	King   Role = 'G'
)

const (
	NumKnightMoves = 8
	NumKingMoves   = 8
)

type Element struct {
	Steps float64
	Role  Role
	Coord [2]int
}

type MinHeap []Element

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i].Steps < h[j].Steps
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Element))
}

func (h *MinHeap) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[0 : n-1]
	return x
}

type Square struct {
	Chip  byte
	Steps float64
}

func traverse(grid [][]Square, start, finish []int, n int) int {
	knightMoves := [NumKnightMoves][2]int{
		{-2, -1}, {-1, -2},
		{1, -2}, {2, -1},
		{2, 1}, {1, 2},
		{-1, 2}, {-2, 1},
	}
	kingMoves := [NumKingMoves][2]int{
		{-1, -1}, {0, -1}, {1, -1},
		{-1, 0}, {1, 0},
		{-1, 1}, {0, 1}, {1, 1},
	}

	pq := &MinHeap{}
	i, j := start[0], start[1]
	heap.Push(pq, Element{Steps: 0, Role: Knight, Coord: [2]int{i, j}})

	for pq.Len() != 0 {
		elem := heap.Pop(pq).(Element)
		currI, currJ := elem.Coord[0], elem.Coord[1]
		currRole := elem.Role

		moveSet := knightMoves
		if currRole == King {
			moveSet = kingMoves
		}

		for _, move := range moveSet {
			nextI, nextJ := currI+move[0], currJ+move[1]
			if !(0 <= nextI && nextI < n && 0 <= nextJ && nextJ < n) {
				continue
			}

			newRole := currRole
			if grid[nextI][nextJ].Chip == 'G' {
				newRole = King
			}
			if grid[nextI][nextJ].Chip == 'K' {
				newRole = Knight
			}

			newSteps := grid[currI][currJ].Steps + 1
			if newSteps < grid[nextI][nextJ].Steps {
				grid[nextI][nextJ].Steps = newSteps
				heap.Push(pq, Element{Steps: newSteps, Role: newRole, Coord: [2]int{nextI, nextJ}})
			}
		}
	}

	i, j = finish[0], finish[1]
	answer := grid[i][j].Steps
	if answer == math.Inf(1) {
		answer = -1
	}

	return int(answer)
}

func main() {
	var n int
	fmt.Scanf("%d", &n)

	startSquare := [2]int{}
	finishSquare := [2]int{}

	grid := make([][]Square, n)
	for i := 0; i < n; i++ {
		var s string
		fmt.Scanf("%s", &s)

		grid[i] = make([]Square, n)
		for j := 0; j < n; j++ {
			grid[i][j].Chip = s[j]
			grid[i][j].Steps = math.Inf(1)

			if s[j] == 'S' {
				startSquare[0], startSquare[1] = i, j
				grid[i][j].Steps = 0
			}
			if s[j] == 'F' {
				finishSquare[0], finishSquare[1] = i, j
			}
		}
	}

	fmt.Println(traverse(grid, startSquare[:], finishSquare[:], n))
}
