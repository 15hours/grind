package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solve(in *bufio.Reader, out *bufio.Writer) {
	var n int
	var k int64
	fmt.Fscan(in, &n, &k)

	var m int
	fmt.Fscan(in, &m)

	in.ReadString('\n')
	line, _ := in.ReadString('\n')
	s := strings.TrimSpace(line)
	arr := strings.Split(s, " ")
	numbers := make([]int, len(arr))

	maxx := 0
	a := make([]int, 30)
	for i, part := range arr {
		num, err := strconv.Atoi(part)
		if err != nil {
			fmt.Println("Error converting to integer:", err)
			return
		}
		numbers[i] = num
		a[numbers[i]]++

		if num > maxx {
			maxx = num
		}
	}

	mLeft := m
	result := 0
	for mLeft > 0 {
		result++
		for i := 0; i < n; i++ {
			sum := k
			for j := maxx; j >= 0; j-- {
				powerOfTwo := int64(1) << int64(j)
				for a[j] > 0 && sum-powerOfTwo >= 0 {
					sum -= powerOfTwo
					a[j]--
					mLeft--
				}
			}
		}
	}
	fmt.Fprintln(out, result)
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
