package main

import (
	"container/heap"
	"fmt"
	"math"
	"math/rand"
	"slices"
)

// time O(n*log(n))
// space O(1)
func findKthLargest(nums []int, k int) int {
	slices.Sort(nums)
	return nums[len(nums)-k]
}

// time O(n²)
// space O(n)
func findKthLargestBFApproach(nums []int, k int) int {
	visited := make(map[int]bool)
	n := len(nums)
	kthLargest := math.MinInt16

	for ; k > 0; k-- {
		curMax := math.MinInt16
		var idx int
		for i := 0; i < n; i++ {
			if !visited[i] && nums[i] >= curMax {
				curMax = nums[i]
				idx = i
			}
		}
		kthLargest = curMax
		visited[idx] = true
	}

	return kthLargest
}

type PriorityQueue []int

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i] < pq[j]
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(int))
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	x := old[n-1]
	*pq = old[0 : n-1]
	return x
}

// time O(n * log k)
// space O(k)
func findKthLargestPriorityQueueApproach(nums []int, k int) int {
	pq := PriorityQueue(nums[:k])
	heap.Init(&pq)

	for _, num := range nums[k:] {
		if num > pq[0] {
			heap.Pop(&pq)
			heap.Push(&pq, num)
		}
	}

	return pq[0]
}

func partition(list []int, left, right, pivotIdx int) int {
	pivotVal := list[pivotIdx]
	list[pivotIdx], list[right] = list[right], list[pivotIdx]
	storeIdx := left

	for i := left; i < right; i++ {
		if list[i] < pivotVal {
			list[storeIdx], list[i] = list[i], list[storeIdx]
			storeIdx++
		}
	}

	list[right], list[storeIdx] = list[storeIdx], list[right]
	return storeIdx
}

func quickSelect(list []int, left, right, k int) int {
	if left == right {
		return list[left]
	}
	pivotIdx := left + rand.Intn(right-left+1)
	newPivotIdx := partition(list, left, right, pivotIdx)

	if newPivotIdx > k {
		quickSelect(list, left, newPivotIdx-1, k)
	} else if newPivotIdx < k {
		quickSelect(list, newPivotIdx+1, right, k)
	}

	return list[k]
}

func findKthLargestQuickSelectApproach(nums []int, k int) int {
	n := len(nums)
	left, right := 0, n-1
	return quickSelect(nums, left, right, n-k)
}

func main() {
	nums1 := []int{3, 2, 1, 5, 6, 4}
	fmt.Println(findKthLargestBFApproach(nums1, 2))

	nums2 := []int{3, 2, 3, 1, 2, 4, 5, 5, 6}
	fmt.Println(findKthLargestBFApproach(nums2, 4))
}
