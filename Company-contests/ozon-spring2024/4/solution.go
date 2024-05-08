package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type Pair struct {
	Time int
	Idx  int
}

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n int
	fmt.Fscan(in, &n)

	t := make([]Pair, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &t[i].Time)
		t[i].Idx = i
	}

	sort.Slice(t, func(i, j int) bool {
		return t[i].Time < t[j].Time
	})

	result := make([]int, n)
	result[t[0].Idx] = 1
	for i := 1; i < n; i++ {
		if t[i].Time-t[i-1].Time <= 1 {
			result[t[i].Idx] = result[t[i-1].Idx]
		} else {
			result[t[i].Idx] = i + 1
		}
	}

	for i := 0; i < n; i++ {
		fmt.Fprint(out, result[i])
		if i < n-1 {
			fmt.Fprint(out, " ")
		}
	}
	fmt.Fprintln(out)
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
