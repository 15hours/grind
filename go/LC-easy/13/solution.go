package main

import (
	"fmt"
)

func romanToInt(s string) int {
	romanNumerals := map[uint8]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	var correspondingInteger, currentSum int

	for i := len(s) - 1; i >= 0; i-- {
		currentValue := romanNumerals[s[i]]

		if currentValue < currentSum {
			correspondingInteger -= currentValue
		} else {
			correspondingInteger += currentValue
		}

		currentSum = currentValue
	}

	return correspondingInteger
}

func main() {
	fmt.Println(romanToInt("III"))
	fmt.Println(romanToInt("LVIII"))
	fmt.Println(romanToInt("MCMXCIV"))
}
