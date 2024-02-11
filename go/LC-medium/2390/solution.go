package main

import "fmt"

func removeStars(s string) string {
	var result []byte
	starCount := 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '*' {
			starCount++
		} else {
			if starCount > 0 {
				starCount--
				continue
			} else {
				result = append(result, s[i])
			}
		}
	}

	n := len(result)
	for i := 0; i < n/2; i++ {
		result[i], result[n-i-1] = result[n-i-1], result[i]
	}

	return string(result)
}

func removeStarsStackApproach(s string) string {
	var stack []byte
	for i := 0; i < len(s); i++ {
		if s[i] != '*' {
			stack = append(stack, s[i])
		} else {
			stack = stack[:len(stack)-1]
		}
	}

	return string(stack)
}

func main() {
	fmt.Println(removeStars("aa*bc**lxl*o"))
	fmt.Println(removeStars("erase*****"))
	fmt.Println(removeStarsStackApproach("aa*bc**lxl*o"))
	fmt.Println(removeStarsStackApproach("erase*****"))
}
