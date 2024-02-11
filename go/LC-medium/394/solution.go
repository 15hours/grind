package main

import (
	"fmt"
	"strings"
)

func decodeString(s string) string {
    sLen := len(s)
    var result strings.Builder

    for i := 0; i < sLen; i++ {

    }
}

func main() {
    fmt.Println(decodeString("3[a]2[bc]"))
    fmt.Println(decodeString("3[a2[c]]"))
    fmt.Println(decodeString("2[abc]3[cd]ef"))
}
