package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	s1, s2 := listSize(l1), listSize(l2)
	diff := s1 - s2
	if s1 < s2 {
		diff = s2 - s1
		l1, l2 = l2, l1
	}

	result := &ListNode{}
	for curNode := result; l1 != nil || l2 != nil; curNode = curNode.Next {
		if diff > 0 {
			curNode.Val = l1.Val
			diff--
			l1 = l1.Next
		} else {
			curNode.Val = l1.Val + l2.Val
			l1, l2 = l1.Next, l2.Next
		}

		if l1 != nil && l2 != nil {
			curNode.Next = &ListNode{}
		}
	}

	resultReversed := reverseList(result)

	answerReversed := &ListNode{}
	carry := 0
	for curNode := answerReversed; resultReversed != nil || carry != 0; curNode = curNode.Next {
		if resultReversed != nil {
			carry += resultReversed.Val
			resultReversed = resultReversed.Next
		}
		curNode.Next = &ListNode{Val: carry % 10}
		carry /= 10
	}

	answer := reverseList(answerReversed.Next)
	return answer
}

func reverseList(head *ListNode) *ListNode {
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

func listSize(l *ListNode) int {
	s := 0
	for l != nil {
		s++
		l = l.Next
	}
	return s
}

func printLinkedList(l *ListNode) {
	for l != nil {
		fmt.Print(l.Val, " ")
		l = l.Next
	}
	fmt.Println()
}

func main() {
	l1 := &ListNode{6, &ListNode{2, &ListNode{3, nil}}}
	l2 := &ListNode{9, &ListNode{5, &ListNode{6, &ListNode{4, nil}}}}
	printLinkedList(addTwoNumbers(l1, l2))
}
