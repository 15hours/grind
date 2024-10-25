package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	carry := 0

	for curNode := result; l1 != nil || l2 != nil || carry != 0; curNode = curNode.Next {
		if l1 != nil {
			carry += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			carry += l2.Val
			l2 = l2.Next
		}

		curNode.Next = &ListNode{Val: carry % 10}
		carry /= 10
	}

	return result.Next
}

func printLinkedList(l *ListNode) {
	for l != nil {
		fmt.Print(l.Val, " ")
		l = l.Next
	}
	fmt.Println()
}

func main() {
	l1 := &ListNode{2, &ListNode{4, &ListNode{3, nil}}}
	l2 := &ListNode{5, &ListNode{6, &ListNode{4, nil}}}
	printLinkedList(addTwoNumbers(l1, l2))
}
