package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Pair struct {
	Val int
	Idx int
}

type PPair struct {
	S   int
	E   int
	C   int
	Idx int
}

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n int
	fmt.Fscan(in, &n)

	in.ReadString('\n')
	line, _ := in.ReadString('\n')
	s := strings.TrimSpace(line)
	arr := strings.Split(s, " ")
	arrival := make([]Pair, n)
	for i := 0; i < n; i++ {
		arrival[i].Val, _ = strconv.Atoi(arr[i])
		arrival[i].Idx = i
	}
	sort.Slice(arrival, func(i, j int) bool {
		return arrival[i].Val < arrival[j].Val
	})

	var m int
	fmt.Fscan(in, &m)

	truck := make([]PPair, m)
	for i := 0; i < m; i++ {
		var s, e, c int
		fmt.Fscan(in, &s, &e, &c)
		truck[i].S = s
		truck[i].E = e
		truck[i].C = c
		truck[i].Idx = i
	}

	sort.Slice(truck, func(i, j int) bool {
		if truck[i].S == truck[j].S {
			return truck[i].Idx < truck[j].Idx
		}
		return truck[i].S < truck[j].S
	})

	p := 0
	result := make([]int, n)
	for i := 0; i < m && p < n; i++ {
		for truck[i].C > 0 && p < n {
			if arrival[p].Val >= truck[i].S && arrival[p].Val <= truck[i].E {
				truck[i].C--
				result[arrival[p].Idx] = truck[i].Idx + 1
				p++
			} else if truck[i].S > arrival[p].Val {
				//fmt.Println(arrival[p].Val, truck[i].S)
				result[arrival[p].Idx] = -1
				p++
			} else { // arrival[p] > truck[i].E
				// fmt.Println("here", p, i, arrival[p].Idx)
				break
			}
		}
	}

	for i := 0; i < n; i++ {
		if result[i] == 0 {
			fmt.Fprint(out, -1)
		} else {
			fmt.Fprint(out, result[i])
		}
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
