// 7. дано две строки, сказать является ли одна ПОДПОСОЕДОВАТЕЛЬНОСТЬЮ другой.
// Тут подпосоедовательность понимается в смысле, что словно выкинуть лишние буквы.

package main

import "fmt"

func isSubstring(w1, w2 string) bool {
	// w1: hello, w2: elo -> true
	// w1: hello, w2: elx -> false

    if len(w2) > len(w1) {
        return false
    }

    j := 0
    for i := 0; i < len(w1) && j < len(w2); i++ {
		if w1[i] == w2[j] {
			j++
		}
	}

	if j < len(w2) {
		return false
	}

	return true
}

func main() {
    fmt.Println(isSubstring("hello", "elo"))
    fmt.Println(isSubstring("hello", "elx"))
    fmt.Println(isSubstring("hello", ""))
    fmt.Println(isSubstring("hello", "world"))
    fmt.Println(isSubstring("hello", "hello"))
}
