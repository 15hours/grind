package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	if !scanner.Scan() {
		return
	}
	firstLine := scanner.Text()
	parts := strings.Fields(firstLine)

	n, _ := strconv.Atoi(parts[0])
	t := parts[1]

	for i := 0; i < n; i++ {
		if !scanner.Scan() {
			return
		}
		rowStr := scanner.Text()
		_ = strings.Fields(rowStr)
	}

	fmt.Println(n / 2 * (n + 1) / 2 * 3)

	for i := 0; i < n/2; i++ {
		for j := 0; j < (n+1)/2; j++ {
			if t == "L" {
				fmt.Printf("%d %d %d %d\n", i, j, j, n-1-i)
				fmt.Printf("%d %d %d %d\n", j, n-1-i, n-1-i, n-1-j)
				fmt.Printf("%d %d %d %d\n", n-1-i, n-1-j, n-1-j, i)
			} else {
				fmt.Printf("%d %d %d %d\n", i, j, n-1-j, i)
				fmt.Printf("%d %d %d %d\n", n-1-j, i, n-1-i, n-1-j)
				fmt.Printf("%d %d %d %d\n", n-1-i, n-1-j, j, n-1-i)
			}
		}
	}
}
