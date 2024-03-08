package main

import (
	"fmt"
	"slices"
)

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	freq1 := [26]int{}
	freq2 := [26]int{}

	for i := 0; i < len(word1); i++ {
		freq1[word1[i]-'a']++
		freq2[word2[i]-'a']++
	}

	for i := 0; i < 26; i++ {
		if freq1[i] != 0 && freq2[i] != 0 || freq1[i] == 0 && freq2[i] == 0 {
			continue
		}
		return false
	}

	slices.Sort(freq1[:])
	slices.Sort(freq2[:])

	return freq1 == freq2
}

func main() {
	fmt.Println(closeStrings("abc", "bca"))
	fmt.Println(closeStrings("cabbba", "abbccc"))
	fmt.Println(closeStrings("a", "aa"))
	fmt.Println(closeStrings("abcde", "bcadz"))
}
