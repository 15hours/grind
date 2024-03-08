package main

import "container/heap"

type MinHeap []int

func (h MinHeap) Len() int {
	return len(h)
}

func (h MinHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type SmallestInfiniteSet struct {
	smallest int
	minHeap  *MinHeap
	inHeap   map[int]bool
}

func Constructor() SmallestInfiniteSet {
	h := &MinHeap{}
	heap.Init(h)
	return SmallestInfiniteSet{0, h, map[int]bool{}}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	if this.minHeap.Len() > 0 {
		pop := heap.Pop(this.minHeap).(int)
		this.inHeap[pop] = false
		return pop
	}

	this.smallest++
	return this.smallest
}

func (this *SmallestInfiniteSet) AddBack(num int) {
	if num <= this.smallest && !this.inHeap[num] {
		this.inHeap[num] = true
		heap.Push(this.minHeap, num)
	}
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */
