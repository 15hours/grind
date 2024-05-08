package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n, t int
	fmt.Fscan(in, &n, &t)

	in.ReadString('\n')
	line, _ := in.ReadString('\n')
	s := strings.TrimSpace(line)
	arr := strings.Split(s, " ")
	m := [26]int{}
	for _, char := range arr {
		if len(char) > 0 && char[0] >= 'a' && char[0] <= 'z' {
			m[char[0]-'a']++
		}
	}

	pass := make([]string, t)
	for i := 0; i < t; i++ {
		var str string
		fmt.Fscan(in, &str)
		pass[i] = str
	}

	for i := 0; i < t; i++ {
		mm := [26]int{}
		for _, char := range pass[i] {
			if char >= 'a' && char <= 'z' {
				mm[char-'a']++
			}
		}

		if m == mm {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
}
