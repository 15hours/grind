package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type Pair struct {
	Val int
	Idx int
}

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, m int
	fmt.Fscan(in, &n, &m)

	a := make([]Pair, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &a[i].Val)
		a[i].Idx = i
	}

	if m <= n {
		fmt.Fprintln(out, -1)
		return
	}

	sort.Slice(a, func(i, j int) bool {
		return a[i].Val > a[j].Val
	})

	result := make([]int, n)

	for i := 0; i < n; i++ {
		if a[i].Val >= m {
			fmt.Fprintln(out, -1)
			return
		}
		result[a[i].Idx] = m
		m--
	}

	for i := 0; i < n; i++ {
		fmt.Fprint(out, result[i])
		if i < n-1 {
			fmt.Fprint(out, " ")
		}
	}
	fmt.Fprintln(out)
}
