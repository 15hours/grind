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
	userMessageStack := make(map[int]int, n)

	everybodyAt := 0
	everybodyAtStack := 0

	currMessage := 0

	for i := 0; i < q; i++ {
		var t, id int
		fmt.Fscan(in, &t, &id)

		switch t {
		case 1:
			currMessage++

			if id == 0 {
				everybodyAt = currMessage
				everybodyAtStack = i + 1
			} else {
				userMessage[id-1] = currMessage
				userMessageStack[id-1] = i + 1
			}
		case 2:
			if userMessageStack[id-1] > everybodyAtStack {
				fmt.Fprintln(out, userMessage[id-1])
			} else {
				fmt.Fprintln(out, everybodyAt)
			}
		}
	}
}
