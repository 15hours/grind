package main

import (
	"container/heap"
	"fmt"
)

type MinHeap1 []int

func (h MinHeap1) Len() int {
	return len(h)
}

func (h MinHeap1) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h MinHeap1) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap1) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap1) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[0 : n-1]
	return x
}

func totalCost(costs []int, k int, candidates int) int64 {
	n := len(costs)
	lr := candidates - 1
	rl := n - candidates

	ans := 0
	if lr >= rl {
		h := MinHeap1(costs)
		heap.Init(&h)
		for k > 0 {
			ans += heap.Pop(&h).(int)
			k--
		}
		return int64(ans)
	}

	h1 := MinHeap1(costs[0 : lr+1])
	heap.Init(&h1)
	h2 := MinHeap1(costs[rl:n])
	heap.Init(&h2)

	for rl-lr > 1 && k > 0 {
		if h1[0] <= h2[0] {
			ans += heap.Pop(&h1).(int)
			lr++
			heap.Push(&h1, costs[lr])
		} else {
			ans += heap.Pop(&h2).(int)
			rl--
			heap.Push(&h2, costs[rl])
		}
		k--
	}

	for k > 0 {
		if len(h1) > 0 && len(h2) > 0 {
			if h1[0] <= h2[0] {
				ans += heap.Pop(&h1).(int)
			} else {
				ans += heap.Pop(&h2).(int)
			}
		} else if len(h1) > 0 {
			ans += heap.Pop(&h1).(int)
		} else {
			ans += heap.Pop(&h2).(int)
		}
		k--
	}

	return int64(ans)

}

func main() {
	fmt.Println(totalCost([]int{17, 12, 10, 2, 7, 2, 11, 20, 8}, 3, 4))
	fmt.Println(totalCost([]int{1, 2, 4, 1}, 3, 3))
	fmt.Println(totalCost([]int{28, 35, 21, 13, 21, 72, 35, 52, 74, 92, 25, 65, 77, 1, 73, 32, 43, 68, 8, 100, 84, 80, 14, 88, 42, 53, 98, 69, 64, 40, 60, 23, 99, 83, 5, 21, 76, 34}, 32, 12))
	fmt.Println(totalCost([]int{57, 33, 26, 76, 14, 67, 24, 90, 72, 37, 30}, 11, 2))
}
