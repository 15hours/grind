package main

func findCircleNum(isConnected [][]int) int {
	count := 0
	numNodes := len(isConnected)
	visited := make([]bool, numNodes)

	var traverse func(node int)
	traverse = func(node int) {
		if visited[node] {
			return
		}
		visited[node] = true

		for nextNode, connected := range isConnected[node] {
			if connected == 0 {
				continue
			}

			traverse(nextNode)
		}
	}

	for node := range visited {
		if visited[node] {
			continue
		}
		count++
		traverse(node)
	}

	return count
}
