package main

import "container/heap"

type MinHeap2 [][]int

func (h MinHeap2) Len() int {
	return len(h)
}

func (h MinHeap2) Less(i, j int) bool {
	if h[i][0] == h[j][0] {
		return h[i][1] < h[j][1]
	}
	return h[i][0] < h[j][0]
}

func (h MinHeap2) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap2) Push(x interface{}) {
	*h = append(*h, x.([]int))
}

func (h *MinHeap2) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[0 : n-1]
	return x
}

func totalCost2(costs []int, k int, candidates int) int64 {
	h := &MinHeap2{}
	for i := 0; i < candidates; i++ {
		heap.Push(h, []int{costs[i], 0})
	}

	n := len(costs)
	for i := max(candidates, n-candidates); i < len(costs); i++ {
		heap.Push(h, []int{costs[i], 1})
	}

	ans := 0
	lr, rl := candidates, n-candidates-1
	for k > 0 {
		candidate := heap.Pop(h).([]int)
		ans += candidate[0]
		turn := candidate[1]

		if lr <= rl {
			if turn == 0 {
				heap.Push(h, []int{costs[lr], 0})
				lr++
			} else {
				heap.Push(h, []int{costs[rl], 1})
				rl--
			}
		}
		k--
	}

	return int64(ans)
}
