package main

import (
	"fmt"
	"unicode"
)

func isVowel(char rune) bool {
	c := unicode.ToLower(char)
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
		c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
}

func reverseVowels(s string) string {
	sSlice := []byte(s)
	l, r := 0, len(s)-1

	for l < r {
		for l < r && !isVowel(rune(s[l])) {
			l++
		}
		for l < r && !isVowel(rune(s[r])) {
			r--
		}
		sSlice[l], sSlice[r] = sSlice[r], sSlice[l]
		l++
		r--
	}

	return string(sSlice)
}

func main() {
	fmt.Println(reverseVowels("hello"))
	fmt.Println(reverseVowels("company"))
}
