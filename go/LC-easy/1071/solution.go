package main

import (
	"fmt"
	"strings"
)

func gcdOfStringsBFApproach(str1 string, str2 string) string {
	var substringBuilder strings.Builder
	var largestSubstring string

	str1Length := len(str1)
	str2Length := len(str2)

	for i := 0; i < str1Length; i++ {
		substringBuilder.WriteRune(rune(str1[i]))
		currentSubstring := substringBuilder.String()
		shiftLength := len(currentSubstring)

		if str1Length%shiftLength != 0 || str2Length%shiftLength != 0 {
			continue
		}

		substringFound := true
		for j := 0; j < str1Length-shiftLength+1; {
			if str1[j:j+shiftLength] != currentSubstring {
				substringFound = false
			}
			j += shiftLength
		}
		for j := 0; j < str2Length-shiftLength+1; {
			if str2[j:j+shiftLength] != currentSubstring {
				substringFound = false
			}
			j += shiftLength
		}

		if substringFound && len(currentSubstring) > len(largestSubstring) {
			largestSubstring = currentSubstring
		}
	}

	return largestSubstring
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func gcdOfStringsMathApproach(str1 string, str2 string) string {
	if str1+str2 != str2+str1 {
		return ""
	}

	gcdOfLengths := gcd(len(str1), len(str2))

	return str1[:gcdOfLengths]
}

func main() {
	str1 := "ABABAB"
	str2 := "ABAB"
	fmt.Println(gcdOfStringsBFApproach(str1, str2))
	fmt.Println(gcdOfStringsMathApproach(str1, str2))

	str3 := "ABCABC"
	str4 := "ABC"
	fmt.Println(gcdOfStringsBFApproach(str4, str3))
	fmt.Println(gcdOfStringsMathApproach(str4, str3))
}
