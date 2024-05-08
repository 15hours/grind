package main

import "fmt"

func isSubsequence(s string, t string) bool {
	sLength, tLength := len(s), len(t)
	sPointer, tPointer := 0, 0

	for sPointer < sLength && tPointer < tLength {
		if t[tPointer] == s[sPointer] {
			sPointer++
		}
		tPointer++
	}

	return sPointer == sLength
}

func main() {
	fmt.Println(isSubsequence("abc", "ahbgdc"))
	fmt.Println(isSubsequence("axc", "ahbgdc"))
}
