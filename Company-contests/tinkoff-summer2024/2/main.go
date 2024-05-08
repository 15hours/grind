package main

import "fmt"

func main() {
	var n, m int

	fmt.Scanf("%d %d", &n, &m)

	rotated := make([][]int64, m)
	for i := 0; i < m; i++ {
		rotated[i] = make([]int64, n)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			var a int64
			fmt.Scanf("%d", &a)
			rotated[j][n-i-1] = a
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j > 0 {
				fmt.Print(" ")
			}
			fmt.Print(rotated[i][j])
		}
		fmt.Println()
	}
}
