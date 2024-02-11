package main

import "fmt"

func productExceptSelf(nums []int) []int {
	n := len(nums)
	result := make([]int, n)

	product := 1
	for i := 0; i < n; i++ {
		result[i] = product
		product *= nums[i]
	}

	product = 1
	for i := n - 1; i >= 0; i-- {
		result[i] *= product
		product *= nums[i]
	}

	return result
}

func main() {
	fmt.Println(productExceptSelf([]int{1, 2, 3, 4}))
	fmt.Println(productExceptSelf([]int{-1, 1, 0, -3, 3}))
}
