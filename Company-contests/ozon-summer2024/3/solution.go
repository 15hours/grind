package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var s string
	fmt.Fscan(in, &s)

	n := len(s)
	if s[0] != s[n-1] {
		fmt.Fprintln(out, "NO")
		return
	}
	if n <= 3 {
		fmt.Fprintln(out, "YES")
		return
	}

	a := s[0]
	for i := 1; i < n-1; i++ {
		if s[i] != a && (s[i+1] != a || s[i-1] != a) {
			fmt.Fprintln(out, "NO")
			return
		}
	}
	fmt.Fprintln(out, "YES")
}

func main() {
	var in *bufio.Reader
	var out *bufio.Writer

	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)
	for i := 0; i < t; i++ {
		solve(in, out)
	}
}
