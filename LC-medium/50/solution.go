package main

import (
	"fmt"
	"math"
)

func myPow(x float64, n int) float64 {
	if n < 0 {
		x = 1 / x
	}
	n = int(math.Abs(float64(n)))

	var result float64 = 1.0

	for n > 0 {
		if n&1 != 0 {
			result *= x
		}

		x *= x
		n >>= 1
	}

	return result
}

func main() {
	fmt.Println(myPow(2, 10))
	fmt.Println(myPow(2.1, 3))
	fmt.Println(myPow(2, -3))
	fmt.Println(myPow(2, -2147483648))
}
