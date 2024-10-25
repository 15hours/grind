package main

import (
	"fmt"
	"strings"
)

func judgeCircle(moves string) bool {
	var verticalMove, horizontalMove int

	for _, char := range moves {
		switch char {
		case 'U':
			verticalMove++
		case 'D':
			verticalMove--
		case 'R':
			horizontalMove++
		case 'L':
			horizontalMove--
		default:
			continue
		}
	}

	return verticalMove == 0 && horizontalMove == 0
}

func judgeCircleUsingStringsCount(moves string) bool {
	return strings.Count(moves, "U") == strings.Count(moves, "D") &&
		strings.Count(moves, "R") == strings.Count(moves, "L")
}

func main() {
	fmt.Println(judgeCircle("UD"))
	fmt.Println(judgeCircle("LL"))
	fmt.Println(judgeCircleUsingStringsCount("UD"))
	fmt.Println(judgeCircleUsingStringsCount("LL"))
}
