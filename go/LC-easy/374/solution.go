package main

import "fmt"

func guess(curr, target int) int {
	if curr < target {
		return 1
	} else if curr > target {
		return -1
	} else {
		return 0
	}
}

func guessNumber(n, target int) int {
	l, r := 1, n

	for l != r {
		m := l + (r-l)/2

		if guessResult := guess(m, target); guessResult == 1 {
			l = m + 1
		} else if guessResult == -1 {
			r = m - 1
		} else {
			return m
		}
	}

	return l
}

func main() {
	fmt.Println(guessNumber(10, 6))
	fmt.Println(guessNumber(1, 1))
	fmt.Println(guessNumber(2, 1))
	fmt.Println(guessNumber(2, 2))
	fmt.Println(guessNumber(4, 2))
}
