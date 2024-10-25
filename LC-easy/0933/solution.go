package main

import "fmt"

type RecentCounter struct {
	requests []int
}

func Constructor() RecentCounter {
	return RecentCounter{}
}

func (this *RecentCounter) Ping(t int) int {
	this.requests = append(this.requests, t)

	// for this.requests[0] < t-3000 {
	// 	this.requests = this.requests[1:]
	// }

	idx := binarySearch(this.requests, t-3000)
	this.requests = this.requests[idx:]

	return len(this.requests)
}

func binarySearch(arr []int, target int) int {
	l, r := 0, len(arr)-1

	for l <= r {
		mid := (l + r) / 2

		if target < arr[mid] {
			r = mid - 1
		} else if target > arr[mid] {
			l = mid + 1
		} else {
			return mid
		}
	}

	return l
}

func main() {
	recentCounter := Constructor()
	fmt.Println(recentCounter.Ping(1))
	fmt.Println(recentCounter.Ping(100))
	fmt.Println(recentCounter.Ping(3001))
	fmt.Println(recentCounter.Ping(3002))
}
