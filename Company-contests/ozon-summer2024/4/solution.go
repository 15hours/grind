package main

import (
	"bufio"
	"fmt"
	"os"
)

type bank struct {
	rd float64
	re float64
	dr float64
	de float64
	er float64
	ed float64
}

func solve(in *bufio.Reader, out *bufio.Writer) {
	banks := [3]bank{}
	for i := 0; i < 3; i++ {
		var a, b float64
		fmt.Fscan(in, &a, &b)
		banks[i].rd = b / a
		fmt.Fscan(in, &a, &b)
		banks[i].re = b / a
		fmt.Fscan(in, &a, &b)
		banks[i].dr = b / a
		fmt.Fscan(in, &a, &b)
		banks[i].de = b / a
		fmt.Fscan(in, &a, &b)
		banks[i].er = b / a
		fmt.Fscan(in, &a, &b)
		banks[i].ed = b / a
	}

	var result float64
	for i := 0; i < 3; i++ {
		r := 1.0
		d := banks[i].rd * 1
		e := banks[i].re * 1
		for j := 0; j < 3; j++ {
			if i == j {
				continue
			}
			e1 := banks[j].re * r
			e2 := banks[j].de * d
			r1 := banks[j].dr * d
			r2 := banks[j].er * e

			for k := 0; k < 3; k++ {
				if i == k || j == k {
					continue
				}
				d1 := banks[k].rd * r
				d2 := banks[k].rd * r1
				d3 := banks[k].rd * r2
				d4 := banks[k].ed * e1
				d5 := banks[k].ed * e2
				d6 := banks[k].ed * e
				result = max(result, d1)
				result = max(result, d2)
				result = max(result, d3)
				result = max(result, d4)
				result = max(result, d5)
				result = max(result, d6)
			}
		}
	}

	fmt.Fprintln(out, result)
}

func max(a, b float64) float64 {
	if a > b {
		return a
	}
	return b
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
