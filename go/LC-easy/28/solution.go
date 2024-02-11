package main

import (
	"fmt"
	"strings"
)

func strStrUsingBF(haystack string, needle string) int {
	for i := 0; i < len(haystack); i++ {
		if haystack[i] == needle[0] {
			for j := 0; j < len(needle); j++ {
				if i+j < len(haystack) && haystack[i+j] == needle[j] {
					if j == len(needle)-1 {
						return i
					}
				} else {
					break
				}
			}
		}
	}

	return -1
}

func strStrUsingSlice(haystack string, needle string) int {
	haystackLength := len(haystack)
	needleLength := len(needle)

	if haystackLength == 0 || needleLength == 0 {
		return -1
	}

	for i := 0; i < haystackLength-needleLength+1; i++ {
		if haystack[i:i+needleLength] == needle {
			return i
		}
	}

	return -1
}

func strStrUsingIndex(haystack string, needle string) int {
	if len(haystack) == 0 || len(needle) == 0 {
		return -1
	}

	return strings.Index(haystack, needle)
}

func main() {
	haystack := "someome"
	needle := "me"
	fmt.Println(strStrUsingBF(haystack, needle))
	fmt.Println(strStrUsingSlice(haystack, needle))
	fmt.Println(strStrUsingIndex(haystack, needle))
}
