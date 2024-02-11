package main

import (
	"fmt"
	"strings"
    "unicode/utf8"
)

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func mergeAlternately(word1 string, word2 string) string {
    var resultBuilder strings.Builder
    numCharacters1 := utf8.RuneCountInString(word1)
    numCharacters2 := utf8.RuneCountInString(word2)
    maxCharacters := max(numCharacters1, numCharacters2)

    for i := 0; i < maxCharacters; i++ {
        if i < numCharacters1 {
            resultBuilder.WriteRune(rune(word1[i]))
        }
        if i < numCharacters2 {
            resultBuilder.WriteRune(rune(word2[i]))
        }
    }

    return resultBuilder.String()
}


func main(){
    fmt.Println(mergeAlternately("hello", "sir"))
}
