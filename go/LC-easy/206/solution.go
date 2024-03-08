package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseListUsingIterations(head *ListNode) *ListNode {
	newHead := &ListNode{}
	newHead = nil

	for head != nil {
		nextNode := head.Next
		head.Next = newHead
		newHead = head
		head = nextNode
	}

	return newHead
}

func reverseListUsingRecursion(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	newHead, _ := recursion(head)
	return newHead
}

func recursion(node *ListNode) (head, tail *ListNode) {
	head, tail = node, node

	if node.Next != nil {
		head, tail = recursion(node.Next)
		node.Next = nil

		tail.Next = node
		tail = node
	}

	return head, tail
}

func printLinkedList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, " ")
		head = head.Next
	}
	fmt.Println()
}

func main() {
	list1 := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}
	reversed1 := reverseListUsingIterations(list1)
	printLinkedList(reversed1)

	list2 := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}
	reversed2 := reverseListUsingRecursion(list2)
	printLinkedList(reversed2)
}
