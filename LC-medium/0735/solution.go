package main

import (
	"fmt"
)

func asteroidCollision(asteroids []int) []int {
	var stack []int

	for p := 0; p < len(asteroids); p++ {
		stackLen := len(stack)
		curr := asteroids[p]
		if stackLen == 0 || stack[stackLen-1] < 0 || curr > 0 {
			stack = append(stack, curr)
			continue
		}

		top := stack[stackLen-1]

		if -curr > top {
			stack = stack[:stackLen-1]
			p--
		} else if -curr == top {
			stack = stack[:stackLen-1]
		}
	}

	return stack
}

func main() {
	fmt.Println(asteroidCollision([]int{5, 10, -20}))
	fmt.Println(asteroidCollision([]int{8, -8}))
	fmt.Println(asteroidCollision([]int{10, 2, -5}))
	fmt.Println(asteroidCollision([]int{-2, -1, 1, 2}))
}
