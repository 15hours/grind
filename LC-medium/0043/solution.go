package main

import "fmt"

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	l1 := len(num1)
	l2 := len(num2)
	result := make([]byte, l1+l2)

	for i := l2 - 1; i >= 0; i-- {
		for j := l1 - 1; j >= 0; j-- {
			val := (num1[j] - '0') * (num2[i] - '0')
			result[i+j+1] += val
			if result[i+j+1] > 9 {
				result[i+j] += result[i+j+1] / 10
				result[i+j+1] %= 10
			}
		}
	}

	if result[0] == 0 {
		result = result[1:]
	}
	for i := range result {
		result[i] += '0'
	}

	return string(result)
}

func main() {
	fmt.Println(multiply("123", "456"))
}
