package main

const (
	Fresh  = 1
	Rotten = 2
)

func orangesRotting(grid [][]int) int {
	queue := [][]int{}

	numRows := len(grid)
	numCols := len(grid[0])
	countFresh := 0
	for i := 0; i < numRows; i++ {
		for j := 0; j < numCols; j++ {
			if grid[i][j] == Rotten {
				queue = append(queue, []int{i, j})
			}

			if grid[i][j] == Fresh {
				countFresh++
			}
		}
	}

	dir := [][]int{
		{-1, 0},
		{0, -1},
		{1, 0},
		{0, 1},
	}

	levels := 0
	for len(queue) != 0 {
		curLevel := queue
		queue = [][]int{}

		for len(curLevel) != 0 {
			curNode := curLevel[0]
			curLevel = curLevel[1:]

			for _, d := range dir {
				di, dj := curNode[0]+d[0], curNode[1]+d[1]
				if !(0 <= di && di < numRows && 0 <= dj && dj < numCols) ||
					grid[di][dj] != Fresh {
					continue
				}

				queue = append(queue, []int{di, dj})
				grid[di][dj] = Rotten
				countFresh--
			}
		}

		if len(queue) != 0 {
			levels++
		}
	}

	if countFresh != 0 {
		return -1
	}
	return levels
}
