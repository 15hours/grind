package main

import (
	"fmt"
	"strings"
)

func toLowerCase(s string) string {
	var resultString strings.Builder

	for i := 0; i < len(s); i++ {
		if 'A' <= s[i] && s[i] <= 'Z' {
			resultString.WriteRune(rune(s[i] - 'A' + 'a'))
			continue
		}
		resultString.WriteRune(rune(s[i]))
	}

	return resultString.String()
}

func main() {
	fmt.Println(toLowerCase("Hello"))
	fmt.Println(toLowerCase("LOVELY"))
}
