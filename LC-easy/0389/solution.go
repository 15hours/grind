package main

import (
	"fmt"
)

func findTheDifferenceUsingMap(s string, t string) byte {
	tMap := make(map[rune]int)

	for _, char := range t {
		tMap[char] += 1
	}
	for _, char := range s {
		tMap[char] -= 1
	}

	for key, value := range tMap {
		if value == 1 {
			return byte(key)
		}
	}

	var zeroByte byte
	return zeroByte
}

func findTheDifferenceUsingBitManipulation(s string, t string) byte {
	sSum := 0
	tSum := 0

	for _, char := range s {
		sSum += int(char)
	}
	for _, char := range t {
		tSum += int(char)
	}

	return byte(tSum - sSum)
}

func main() {
	s := "hello"
	t := "hellno"
	fmt.Println(findTheDifferenceUsingMap(s, t))
	fmt.Println(findTheDifferenceUsingBitManipulation(s, t))
}
