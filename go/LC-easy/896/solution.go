package main

import (
    "fmt"
)

func isMonotonic(nums []int) bool {
    isIncreasing := false
    isDecreasing := false

    for i := 1; i < len(nums); i++ {
        if nums[i] > nums[i - 1] {
            isIncreasing = true
        } else if nums[i] < nums[i - 1] {
            isDecreasing = true
        }

        if isIncreasing && isDecreasing {
            return false
        }
    }

    return true
}

func main() {
    fmt.Println(isMonotonic([]int{1, 2, 2, 3}))
    fmt.Println(isMonotonic([]int{6, 5, 4, 4}))
    fmt.Println(isMonotonic([]int{9, 9, 9, 9, 5}))
    fmt.Println(isMonotonic([]int{9, 9, 9, 9}))
    fmt.Println(isMonotonic([]int{1, 3, 2}))
}
