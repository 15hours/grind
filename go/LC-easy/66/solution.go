package main

import (
    "fmt"
)

func plusOne(digits []int) []int {
    numberLength := len(digits)
    summand := 1

    for i := numberLength - 1; i >= 0; i-- {
        if digits[i] + summand == 10 {
            digits[i] = 0
            summand = 1
        } else {
            digits[i] += summand
            summand = 0
            break
        }
    }

    if summand != 0 {
        return append([]int{summand}, digits...)
    }

    return digits
}

func main() {
    fmt.Println(plusOne([]int{1, 2, 9}))
    fmt.Println(plusOne([]int{1, 9, 9}))
    fmt.Println(plusOne([]int{9, 9, 9}))
}
