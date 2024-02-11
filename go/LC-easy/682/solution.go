package main

import (
	"fmt"
	"slices"
	"strconv"
)

func calPoints(operations []string) int {
	var records []int
    var recordsLength int

    for _, op := range operations {
        switch op {
        case "C":
			records = slices.Delete(records, recordsLength-1, recordsLength)
            recordsLength--
        case "D":
            num := records[recordsLength-1]
            records = append(records, 2*num)
            recordsLength++
        case "+":
            num1 := records[recordsLength-1]
            num2 := records[recordsLength-2]
			records = append(records, num1+num2)
            recordsLength++
        default:
			num, _ := strconv.Atoi(op)
			records = append(records, num)
            recordsLength++
		}
	}

	var score int

	for _, record := range records {
		score += record
	}

	return score
}

func main() {
	fmt.Println(calPoints([]string{"5", "2", "C", "D", "+"}))
	fmt.Println(calPoints([]string{"5", "-2", "4", "C", "D", "9", "+", "+"}))
}
