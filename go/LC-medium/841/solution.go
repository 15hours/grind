package main

import "fmt"

func canVisitAllRooms(rooms [][]int) bool {
	numRooms := len(rooms)
	visited := make([]bool, numRooms)

	var traverse func(node int)
	traverse = func(node int) {
		if visited[node] {
			return
		}

		visited[node] = true

		for _, nextNode := range rooms[node] {
			traverse(nextNode)
		}
	}

	traverse(0)

	for _, v := range visited {
		if !v {
			return false
		}
	}

	return true
}

func main() {
	rooms1 := [][]int{
		{1, 3},
		{3, 0, 1},
		{2},
		{0},
	}

	rooms2 := [][]int{
		{1},
		{2},
		{3},
		{},
	}

	fmt.Println(canVisitAllRooms(rooms1))
	fmt.Println(canVisitAllRooms(rooms2))
}
