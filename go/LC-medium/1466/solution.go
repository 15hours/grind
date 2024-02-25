package main

import (
	"fmt"
	"slices"
)

// time O(n)
// space O(n)
func minReorder(n int, connections [][]int) int {
    trueAdjMap := make(map[int][]int)
	bidirAdjMap := make(map[int][]int)

	for _, connection := range connections {
		node, nextNode := connection[0], connection[1]
        trueAdjMap[node] = append(trueAdjMap[node], nextNode)
		bidirAdjMap[node] = append(bidirAdjMap[node], nextNode)
		bidirAdjMap[nextNode] = append(bidirAdjMap[nextNode], node)
	}

    visited := make([]bool, n)
    var traverse func(node int) int
    traverse = func(node int) int {
        visited[node] = true

        cnt := 0
        for _, nextNode := range bidirAdjMap[node] {
            if visited[nextNode] {
                continue
            }

            needChange := 0
            if !slices.Contains(trueAdjMap[nextNode], node) {
                needChange = 1
            }
            cnt += needChange + traverse(nextNode)
        }

        return cnt
    }

    return traverse(0)
}

func main() {
	connections1 := [][]int{
		{0, 1},
		{1, 3},
		{2, 3},
		{4, 0},
		{4, 5},
	}
	fmt.Println(minReorder(6, connections1))

	connections2 := [][]int{
		{1, 0},
		{1, 2},
		{3, 2},
		{3, 4},
	}
    fmt.Println(minReorder(5, connections2))
}
