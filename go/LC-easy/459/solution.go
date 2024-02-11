package main

import (
	"fmt"
	"strings"
)

func repeatedSubstringPattern(s string) bool {
    if len(s) == 0 {
        return false
    }

    size := len(s)
    sFold := s[1:size] + s[0:size-1]
    fmt.Println(sFold)

    var substringBuilder strings.Builder

    for i := 0; i < len(s) / 2; i++ {
        substringBuilder.WriteRune(rune(s[i]))
        substringLength := i + 1
        substringRepeated := true

        for j := substringLength; j < len(s) - substringLength + 1; j += substringLength {
            if s[j:j + substringLength] != substringBuilder.String() {
                substringRepeated = false
                break
            }
        }

        if substringRepeated && len(s) % substringLength == 0 {
            return true
        }
    }

    return false
}

func main() {
    repeatedSubstringPattern("hello")
    fmt.Println()
}
