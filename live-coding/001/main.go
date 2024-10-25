// 1. умножение большого числа(big number) на 1<=digit<=9

package main

import (
	"fmt"
	"strconv"
)

func main() {
	a := "123456789123456789123456789123456789"
	digit := 7

	carry := 0
	result := ""

	for i := len(a) - 1; i >= 0; i-- {
		x, _ := strconv.Atoi(string(a[i]))

		currProduct := x*digit + carry

		result = strconv.Itoa(currProduct%10) + result
		carry = currProduct / 10
	}

	if carry != 0 {
		result = strconv.Itoa(carry) + result
	}

	fmt.Println(result)
}
