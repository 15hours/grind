package main

import "fmt"

func minDistance(word1 string, word2 string) int {
    var minDistance func(word1, word2 string) int
    minDistance = func(word1, word2 string) int {
        fmt.Println(word1, word2)
        if len(word1) == 0 && len(word2) == 0 {
            return 0
        }
        if len(word1) == 0 {
            return len(word2)
        }
        if len(word2) == 0 {
            return len(word1)
        }

        if word1[0] == word2[0] {
            return minDistance(word1[1:], word2[1:])
        }

        ins := 1 + minDistance(word1, word2[1:])
        del := 1 + minDistance(word1[1:], word2)
        repl := 1 + minDistance(word1[1:], word2[1:])

        return min(ins, del, repl)
    }

    return minDistance(word1, word2)
}

func main() {
    fmt.Println(minDistance("horse", "ros"))
}
