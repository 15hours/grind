package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	n := len(s)
	var result string
	for i := 0; i < n; {
		for i < n && s[i] == ' ' {
			i++
		}
		if i == n {
			break
		}

		j := i
		for j < n && s[j] != ' ' {
			j++
		}

		if len(result) == 0 {
			result = s[i:j]
		} else {
			result = s[i:j] + " " + result
		}

		i = j + 1
	}

	return result
}

func reverseWordsBuiltinApproach(s string) string {
	words := strings.Fields(s)

	l, r := 0, len(words)-1
	for l < r {
		words[l], words[r] = words[r], words[l]
		l++
		r--
	}

	return strings.Join(words, " ")
}

func main() {
	fmt.Println(reverseWords("the sky is blue"))
	fmt.Println(reverseWords("  hello world  "))
	fmt.Println(reverseWords("a good   example"))
}
