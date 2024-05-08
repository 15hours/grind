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

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n, m int
	fmt.Fscan(in, &n, &m)

	w := make([]Pair, m)
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &w[i].Val)
		w[i].Idx = i
	}

	sort.Slice(w, func(i, j int) bool {
		return w[i].Val < w[j].Val
	})

	result := make([]string, n)

	switch w[0].Val {
	case 1:
		result[w[0].Idx] = "0"
	default:
		result[w[0].Idx] = "-"
		w[0].Val--
	}

	for i := 1; i < m; i++ {
		if w[i].Val < w[i-1].Val {
			fmt.Fprintln(out, "x")
			return
		}

		switch w[i].Val - w[i-1].Val {
		case 0:
			result[w[i].Idx] = "+"
			w[i].Val++
			if w[i].Val > n {
				fmt.Fprintln(out, "x")
				return
			}
		case 1:
			result[w[i].Idx] = "0"
		default:
			result[w[i].Idx] = "-"
			w[i].Val--
		}
	}

	for i := 0; i < m; i++ {
		fmt.Fprint(out, result[i])
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
