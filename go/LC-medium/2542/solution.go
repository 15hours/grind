package main

import (
	"container/heap"
	"fmt"
	"sort"
)

type Pair struct {
	Value1 int
	Value2 int
}

type MinHeap []Pair

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i].Value1 < h[j].Value1
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Pair))
}

func (h *MinHeap) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[0 : n-1]
	return x
}

func maxScore(nums1 []int, nums2 []int, k int) int64 {
	n := len(nums1)
	pairs := make(MinHeap, n)
	for i := range nums1 {
		pairs[i] = Pair{nums1[i], nums2[i]}
	}

	sort.Slice(pairs, func(i, j int) bool {
		return pairs[i].Value2 > pairs[j].Value2
	})

	nums1Sum := 0
	minHeap := &MinHeap{}
	for i := 0; i < k; i++ {
		nums1Sum += pairs[i].Value1
		heap.Push(minHeap, pairs[i])
	}

	maxResult := nums1Sum * pairs[k-1].Value2
	for i := k; i < n; i++ {
		smallest := heap.Pop(minHeap).(Pair)
		nums1Sum -= smallest.Value1

		nums1Sum += pairs[i].Value1
		heap.Push(minHeap, pairs[i])

		maxResult = max(maxResult, nums1Sum*pairs[i].Value2)
	}

	return int64(maxResult)
}

func main() {
	fmt.Println(maxScore([]int{1, 3, 3, 2}, []int{2, 1, 3, 4}, 3))
}
