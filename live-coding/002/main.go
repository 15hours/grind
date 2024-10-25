// 2. Реализовать очередь, в которой две операции:
// вставка за 1
// получение первого уникального элемента за 1
package main

import "fmt"


type myQueue struct {
   allElements []int
   uniqueElements []int
   counter map[int]int
   index map[int]int
}

func Constructor() myQueue {
    return myQueue{
        allElements: []int{},
        uniqueElements: []int{},
        counter: make(map[int]int),
        index: make(map[int]int),
    }
}

func (q *myQueue) push(x int) {
    q.allElements = append(q.allElements, x)
   
    q.counter[x]++
   
    if q.counter[x] == 1 {
       q.uniqueElements = append(q.uniqueElements, x)
       q.index[x]  = len(q.uniqueElements) - 1
    } else {
        //idx := q.index[x]
        
    }
   
}

func (q *myQueue) peekUnique() int {

    return 0
}

func main() {
    obj := Constructor()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(1)
    
    fmt.Println(obj.peekUnique())
}
