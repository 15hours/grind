package main

import "fmt"

func average(salary []int) float64 {
	maxSalary, minSalary := salary[0], salary[0]
	avgSalary := 0

	for _, num := range salary {
		avgSalary += num

		if num > maxSalary {
			maxSalary = num
		}
		if num < minSalary {
			minSalary = num
		}
	}

	return float64(avgSalary-maxSalary-minSalary) / float64(len(salary)-2)
}

func main() {
	fmt.Println(average([]int{4000, 3000, 1000, 2000}))
	fmt.Println(average([]int{48000, 59000, 99000, 13000, 78000, 45000, 31000, 17000, 39000, 37000,
		93000, 77000, 33000, 28000, 4000, 54000, 67000, 6000, 1000, 11000}))
}
