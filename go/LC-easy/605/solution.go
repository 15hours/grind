package main

import "fmt"

func canPlaceFlowers(flowerbed []int, n int) bool {
	flowersLeft := n
	flowerbedLength := len(flowerbed)

	for i, plot := range flowerbed {
        if flowersLeft == 0 {
            return true
        }

		if plot == 1 {
			continue
		}

		if (i == 0 || flowerbed[i-1] == 0) &&
			(i == flowerbedLength-1 || flowerbed[i+1] == 0) {
            flowerbed[i] = 1
			flowersLeft--
		}
	}

	if flowersLeft == 0 {
		return true
	}
	return false
}

func main() {
	fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 1))
	fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 2))
}
