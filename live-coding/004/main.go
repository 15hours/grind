// 4. Найти подмассив в массиве с суммой элементов равной target
package main

import "fmt"

func findTargetSum1(nums []int, target int) []int {
    sumMap := make(map[int]int)
    currSum := 0
    
    for i := 0; i < len(nums); i++ {
        currSum += nums[i]
        
        if currSum == target {
            return nums[0:i+1]
        }
        
        if startIndex, ok := sumMap[currSum - target]; ok {
            return nums[startIndex+1: i+1]
        }

        sumMap[currSum] = i
    }
    
    return []int{}
}

func findTargetSum2(nums []int, target int) []int {
    currSum := 0
    
    l := 0
    for r := 0; r < len(nums); r++ {
        currSum += nums[r]
        
        for currSum > target && l <= r {
           currSum -= nums[l]
           l++ 
        }
        
        if currSum == target {
            return nums[l:r+1]
        }
    }
    
    return []int{}
}

func main() {
    fmt.Println(findTargetSum1([]int{1,2,3,4,5}, 9)) // []int{2,3,4}
    fmt.Println(findTargetSum2([]int{1,2,3,4,5}, 9)) // []int{2,3,4}
    
    fmt.Println(findTargetSum1([]int{0}, 9)) // []int{}
    fmt.Println(findTargetSum2([]int{0}, 9)) // []int{}
    
    fmt.Println(findTargetSum1([]int{1,2,3}, 6)) // []int{1,2,3} 
    fmt.Println(findTargetSum2([]int{1,2,3}, 6)) // []int{1,2,3} 
    
    fmt.Println(findTargetSum1([]int{1,2,3,2,5}, 2)) // []int{2}
    fmt.Println(findTargetSum2([]int{1,2,3,2,5}, 2)) // []int{2}
}
