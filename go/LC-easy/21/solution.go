package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	mergedLists := &ListNode{}
	currentNode := mergedLists

	for list1 != nil || list2 != nil {
		if list1 == nil {
			currentNode.Next = list2
			list2 = nil
			continue
		}
		if list2 == nil {
			currentNode.Next = list1
			list1 = nil
			continue
		}

		if list1.Val < list2.Val {
			currentNode.Next = list1
			list1 = list1.Next
		} else {
			currentNode.Next = list2
			list2 = list2.Next
		}

		currentNode = currentNode.Next
	}

	return mergedLists.Next
}

func printLinkedList(list *ListNode) {
	for list != nil {
		fmt.Print(list.Val, " ")
		list = list.Next
	}
	fmt.Println()
}

func main() {
	list1 := &ListNode{1, &ListNode{3, &ListNode{5, nil}}}
	list2 := &ListNode{2, &ListNode{4, &ListNode{6, nil}}}
	mergedLists1 := mergeTwoLists(list1, list2)
	printLinkedList(mergedLists1)

	list3 := &ListNode{1, &ListNode{3, &ListNode{5, nil}}}
	list4 := &ListNode{4, &ListNode{6, nil}}
	mergedLists2 := mergeTwoLists(list3, list4)
	printLinkedList(mergedLists2)
}
