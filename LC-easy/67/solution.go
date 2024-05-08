package main

import (
	"fmt"
	"math/big"
	"strings"
)

func addBinary(a string, b string) string {
	var binarySumReversed strings.Builder
	var carry int
	rightPointerA := len(a) - 1
	rightPointerB := len(b) - 1

	for rightPointerA >= 0 || rightPointerB >= 0 || carry == 1 {
		if rightPointerA >= 0 {
			carry += int(a[rightPointerA] - '0')
			rightPointerA--
		}
		if rightPointerB >= 0 {
			carry += int(b[rightPointerB] - '0')
			rightPointerB--
		}
		binarySumReversed.WriteRune(rune('0' + carry%2))
		carry /= 2
	}

	result := binarySumReversed.String()

	resultLength := len(result)

	binarySum := make([]rune, resultLength)
	for i, char := range result {
		binarySum[resultLength-i-1] = char
	}

	return string(binarySum)
}

func addBinaryUsingBuiltin(a string, b string) string {
	aInt, bInt := new(big.Int), new(big.Int)
	sum := new(big.Int)

	aInt.SetString(a, 2)
	bInt.SetString(b, 2)
	sum.Add(aInt, bInt)

	return sum.Text(2)
}

func main() {
	fmt.Println(addBinary("11", "1"))
	fmt.Println(addBinary("1010", "1011"))

	fmt.Println(addBinaryUsingBuiltin("11", "1"))
	fmt.Println(addBinaryUsingBuiltin("1010", "1011"))
}
