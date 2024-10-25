package main

import "fmt"

func countConsistentStrings(allowed string, words []string) int {
	m1 := make(map[rune]bool)

	for _, char := range allowed {
		m1[char] = true
	}

	cnt := 0
	for _, w := range words {
		cnt++

		for _, char := range w {
			if !m1[char] {
				cnt--
				break
			}
		}
	}

	return cnt
}

func main() {
	allowed := "ab"
	words := []string{"ad","bd","aaab","baa","badab"}
	fmt.Println(countConsistentStrings(allowed, words))
}
