package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
    var in *bufio.Reader
    var out *bufio.Writer
    in = bufio.NewReader(os.Stdin)
    out = bufio.NewWriter(os.Stdout)
    defer out.Flush()

    var n, q int
    fmt.Fscan(in, &n, &q)

    userMessage := make(map[int]int, n)
    messageNum := 1

    for i := 0; i < q; i++ {
        var t, id int
        fmt.Fscan(in, &t, &id)

        switch t {
        case 1:
            switch id {
            case 0:
                for j := 0; j < n; j++ {
                    userMessage[j] = messageNum
                }
            default:
                userMessage[id] = messageNum
            }
            messageNum++
        case 2:
            fmt.Println(userMessage[id])
        }
    }
}
