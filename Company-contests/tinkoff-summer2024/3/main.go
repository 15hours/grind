package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	var n int
	fmt.Scanf("%d", &n)

	sortedPaths := []string{}
	for i := 0; i < n; i++ {
		var s string
		fmt.Scan(&s)
		sortedPaths = append(sortedPaths, s)
	}
	sort.Strings(sortedPaths)

	for _, path := range sortedPaths {
		parts := strings.Split(path, "/")

		depth := len(parts)
		prefix := strings.Repeat("  ", depth-1)
		fmt.Printf("%s%s\n", prefix, parts[depth-1])
	}
}
