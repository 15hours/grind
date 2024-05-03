package main

import "fmt"

func min(a, b int) int {
    if a > b {
        return b
    }
    return a
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
	var n int
	fmt.Scanf("%d", &n)

	grades := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &grades[i])
	}

	count5 := 0
	count23 := 0
	l, r := 0, 0
	for ; r < min(n, 7); r++ {
		if grades[r] == 5 {
			count5++
		}
		if grades[r] <= 3 {
			count23++
		}
	}

	answer := -1
	if count23 == 0 {
		answer = count5
	}

	for ; r < n; r++ {
		if grades[l] == 5 {
			count5--
		}
		if grades[l] <= 3 {
			count23--
		}
		l++

		if grades[r] == 5 {
			count5++
		}
		if grades[r] <= 3 {
			count23++
		}

		if count23 == 0 {
			answer = max(answer, count5)
		}
	}

    fmt.Println(answer)
}
