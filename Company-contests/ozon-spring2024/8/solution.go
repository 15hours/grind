package main

import (
	"bufio"
	"fmt"
	"os"
)

type SubstrCount struct {
	cnt map[string]int
}

func (sc *SubstrCount) countSubstrings(word string) {
	tmp := make(map[string]int)

	for i := 0; i < len(word); i++ {
		for j := i + 1; j <= len(word); j++ {
			substring := word[i:j]
			_, ok := tmp[substring]
			if ok {
				continue
			}
			tmp[substring]++
			sc.cnt[substring]++
		}
	}
}

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n, b, r, f int
	fmt.Fscan(in, &n, &b, &r, &f)

	lines := make([]string, n)
	for i := 0; i < n; i++ {
		var s string
		fmt.Fscan(in, &s)
		lines[i] = s
	}

	var blueSubstr SubstrCount
	blueSubstr.cnt = make(map[string]int)
	for i := 0; i < b; i++ {
		blueSubstr.countSubstrings(lines[i])
	}

	var redSubstr SubstrCount
	redSubstr.cnt = make(map[string]int)
	for i := 0; i < r; i++ {
		redSubstr.countSubstrings(lines[b+i])
	}

	blackWord := lines[f-1]
	for i := 0; i < len(blackWord); i++ {
		for j := i + 1; j <= len(blackWord); j++ {
			substring := blackWord[i:j]
			delete(blueSubstr.cnt, substring)
			delete(redSubstr.cnt, substring)
		}
	}

	for _, word := range lines {
		delete(blueSubstr.cnt, word)
		delete(redSubstr.cnt, word)
	}

	diff := 0
	var result string
	counted := make(map[string]bool)
	for key1, val1 := range blueSubstr.cnt {
		counted[key1] = true
		currDiff := val1 - redSubstr.cnt[key1]
		if currDiff > diff {
			diff = currDiff
			result = key1
		}
	}

	if result == "" {
		result = "whatever"
		diff = 0
	}

	fmt.Fprintln(out, result, diff)
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
