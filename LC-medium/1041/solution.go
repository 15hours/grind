package main

import "fmt"

func isRobotBounded(instructions string) bool {
	dirX, dirY := 0, 1
	x, y := 0, 0

	for i := 0; i < len(instructions); i++ {
		instruction := instructions[i]

		switch instruction {
		case 'L':
			dirX, dirY = -1*dirY, dirX
		case 'R':
			dirX, dirY = dirY, -1*dirX
		case 'G':
			x += dirX
			y += dirY
		}
	}

	if (x == 0 && y == 0) || (dirX != 0 || dirY != 1) {
		return true
	}

	return false
}

func main() {
	fmt.Println(isRobotBounded("GGLLGG"))
	fmt.Println(isRobotBounded("GG"))
	fmt.Println(isRobotBounded("GL"))
	fmt.Println(isRobotBounded("GLGRGR"))
	fmt.Println(isRobotBounded("GLGRG"))
}
