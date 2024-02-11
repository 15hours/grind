package main

import (
	"fmt"
)

func isAnagram(s string, t string) bool {
    if len(s) != len(t) || len(s) == 0 || len(t) == 0 {
        return false
    }

    count := make([]int, 26)

    for i := 0; i < len(s); i++ {
        count[int(s[i]) - int('a')]++
        count[int(t[i]) - int('a')]--
    }

    for _, value := range count {
        if value != 0 {
            return false
        }
    }

    return true
}

func main() {
    s := "a"
    t := "ab"
    fmt.Println(isAnagram(s, t))
}
