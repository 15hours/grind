package main

import "slices"

func kidsWithCandies(candies []int, extraCandies int) []bool {
    candiesLength := len(candies)
    resultArray := make([]bool, candiesLength)
    maxCandies := slices.Max(candies)

    for i := 0; i < candiesLength; i++ {
        if candies[i] + extraCandies >= maxCandies {
            resultArray[i] = true
        } else {
            resultArray[i] = false
        }
    }

    return resultArray
}
