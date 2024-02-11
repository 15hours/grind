package main

import "fmt"

func lemonadeChange(bills []int) bool {
	countFives := 0
	countTens := 0

	for _, bill := range bills {
		if bill == 10 {
			if countFives >= 1 {
				countFives--
			} else {
				return false
			}
			countTens++
		} else if bill == 20 {
            if countTens >= 1 && countFives >= 1 {
                countTens--
                countFives--
            } else if countFives >= 3 {
				countFives -= 3
			} else {
				return false
			}
		} else {
			countFives++
		}
	}

	return true
}

func main() {
	fmt.Println(lemonadeChange([]int{5, 5, 5, 10, 20}))
	fmt.Println(lemonadeChange([]int{5, 5, 10, 10, 20}))
}
