package main

import (
	"fmt"
	"strconv"
	"strings"
)

func decodeString(s string) string {
    kStack := []int{}
    strStack := []string{}
    k := 0
    curStr := ""
    for _, ch := range s {
        if num, err := strconv.Atoi(string(ch)); err == nil {
            k = num + k*10
            continue
        }

        if ch == '[' {
            kStack = append(kStack, k)
            strStack = append(strStack, curStr)
            k = 0
            curStr = ""
        } else if ch == ']' {
            tmp := curStr
            strStackLen := len(strStack)
            curStr = strStack[strStackLen - 1]
            strStack = strStack[:strStackLen - 1]

            kStackLen := len(kStack)
            curStr += strings.Repeat(tmp, kStack[kStackLen - 1])
            kStack = kStack[:kStackLen - 1]
        } else {
            curStr += string(ch)
        }
    }

    return curStr
}

func main() {
    fmt.Println(decodeString("3[a]2[bc]"))
    fmt.Println(decodeString("3[a2[c]]"))
    fmt.Println(decodeString("2[abc]3[cd]ef"))
}
