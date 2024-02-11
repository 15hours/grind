package main

import "fmt"

func compress(chars []byte) int {
	i := 0
	writeIndex := 0

	for i < len(chars) {
		curr := chars[i]
		count := 0

		for j := i; j < len(chars) && chars[j] == curr; j++ {
			count++
		}

		writeIndex++

		if count > 1 {
			countStr := []byte(fmt.Sprintf("%d", count))
			copy(chars[writeIndex:], countStr)
			writeIndex += len(countStr)
			chars = append(chars[:writeIndex], chars[i+count:]...)
			i += len(countStr) + 1
		} else {
			i++
		}
	}

	return len(chars)
}

func main() {
	fmt.Println(compress([]byte{'a', 'a', 'a', 'b'}))
	fmt.Println(compress([]byte{'a', 'a', 'b', 'b', 'c', 'c', 'c'}))
	fmt.Println(compress([]byte{'a'}))
	fmt.Println(compress([]byte{'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a', 'b', 'b'}))
}
