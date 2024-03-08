package main

import (
	"fmt"
)

func lengthOfLastWord(s string) int {
	var resultLength int

	for i := len(s) - 1; i >= 0; i-- {
		if resultLength == 0 && s[i] == ' ' {
			continue
		} else if s[i] != ' ' {
			resultLength++
		} else {
			break
		}
	}

	return resultLength
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
	fmt.Println(lengthOfLastWord("   fly me   to   the moon  "))
}
