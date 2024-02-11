package main

import (
	"fmt"
	"slices"
	// "sort"
)

func selectionSort(arr []int) []int {
	numElements := len(arr)

	for i := 0; i < numElements; i++ {
		indexOfMinValue := i

		for j := i + 1; j < numElements; j++ {
			if arr[j] < arr[indexOfMinValue] {
				indexOfMinValue = j
			}
		}

		arr[i], arr[indexOfMinValue] = arr[indexOfMinValue], arr[i]
	}

	return arr
}

func bubbleSort(arr []int) []int {
	numElements := len(arr)

	for hasSwapped := true; hasSwapped; {
		hasSwapped = false

		for j := 0; j < numElements-1; j++ {
			if arr[j+1] < arr[j] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				hasSwapped = true
			}
		}
	}

	return arr
}

func insertionSort(arr []int) []int {
	numElements := len(arr)

	for i := 1; i < numElements; i++ {
		curElement := arr[i]
		j := i

		for j > 0 && arr[j-1] > curElement {
			arr[j] = arr[j-1]
			j--
		}

		arr[j] = curElement
	}

	return arr
}

func heapSort(arr []int) []int {
	numNodes := len(arr)

	var maxHeapify func(heapSize, nodeIndex int)

	maxHeapify = func(heapSize, nodeIndex int) {
		leftNodeIndex := 2*nodeIndex + 1
		rightNodeIndex := 2*nodeIndex + 2
		indexOfLargestValue := nodeIndex

		if leftNodeIndex < heapSize && arr[leftNodeIndex] > arr[indexOfLargestValue] {
			indexOfLargestValue = leftNodeIndex
		}
		if rightNodeIndex < heapSize && arr[rightNodeIndex] > arr[indexOfLargestValue] {
			indexOfLargestValue = rightNodeIndex
		}
		if indexOfLargestValue != nodeIndex {
			arr[nodeIndex], arr[indexOfLargestValue] = arr[indexOfLargestValue], arr[nodeIndex]
			maxHeapify(heapSize, indexOfLargestValue)
		}
	}

	for i := numNodes/2 - 1; i >= 0; i-- {
		maxHeapify(numNodes, i)
	}

	for i := numNodes - 1; i > 0; i-- {
		arr[i], arr[0] = arr[0], arr[i]
		maxHeapify(i, 0)
	}

	return arr
}

func canMakeArithmeticProgression(arr []int) bool {
	// sortedArr := selectionSort(arr)
	// sortedArr := bubbleSort(arr)
	// sortedArr := insertionSort(arr)
	// sortedArr := heapSort(arr)

	// sortedArr := make([]int, len(arr))
	// copy(sortedArr, arr)
	// sort.Ints(sortedArr)

	sortedArr := make([]int, len(arr))
	copy(sortedArr, arr)
	slices.Sort(sortedArr)

	targetDiff := sortedArr[1] - sortedArr[0]

	for i := 1; i < len(sortedArr); i++ {
		if sortedArr[i]-sortedArr[i-1] != targetDiff {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(canMakeArithmeticProgression([]int{3, 5, 1}))
	fmt.Println(canMakeArithmeticProgression([]int{1, 2, 4}))
	fmt.Println(canMakeArithmeticProgression([]int{-68, -96, -12, -40, 16}))
}
