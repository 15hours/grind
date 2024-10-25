package main

import "fmt"

func lineExists(points [][]int) bool {
    if len(points) == 1 {
        return true
    }

    pSet := make(map[[2]int]bool)

    minX := points[0][0]
    maxX := points[0][0]

    for _, p := range points {
        minX = min(minX, p[0])
        maxX = max(maxX, p[0])
        pSet[[2]int{p[0], p[1]}] = true
    }
    
    pivot := (minX + maxX) / 2
    
    for _, p := range points {
        x, y := p[0], p[1]
        if x < pivot {
            if !pSet[[2]int{pivot + (pivot - x), y}] {
                return false
            }
        } else {
            if !pSet[[2]int{pivot - (pivot - x), y}] {
                return false
            }
        }
    }
    
    return true
    
    // map x,y : bool
    // условие несуществования линии: точка, для которой нет отзеркаленной, т.е. для какой-то x1,y не должна существовать x2,y , т.е для (pivot - x1), y не найдейтся x2, y
    // pivot := (maxX + minX) / 2
    // for x, y := points
    // if x < pivot: if !points[pivot + (pivot - x)][y]
    // if x > pivot: if !poi
    // if !points[pivot - x][y] {
    //    return false
    // }
    // 
    // return true
}

func main() {
    fmt.Println(lineExists([][]int{
        {-1, 0},
        {1, 0},
    })) // true
    
    fmt.Println(lineExists([][]int{
        {-2, 0},
        {1, 0},
    })) // false
}
