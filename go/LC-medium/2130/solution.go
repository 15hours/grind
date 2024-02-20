package main

import "fmt"

type ListNode struct {
    Val int
    Next *ListNode
}

func pairSumBFApproach(head *ListNode) int {
    nodeValues := []int{}

    for head != nil {
        nodeValues = append(nodeValues, head.Val)
        head = head.Next
    }

    numNodes := len(nodeValues)
    maxSum := 0
    for i := 0; i < numNodes / 2; i++ {
        twinSum := nodeValues[i] + nodeValues[numNodes - i - 1]
        if twinSum > maxSum {
            maxSum = twinSum
        }
    }

    return maxSum
}

func pairSumReverseListApproach(head *ListNode) int {
    slow, fast := head, head

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    reversedHalf := reverseLinkedList(slow)
    originalHead := head

    maxSum := 0
    for reversedHalf != nil {
        curSum := reversedHalf.Val + originalHead.Val
        if curSum > maxSum {
            maxSum = curSum
        }
        reversedHalf = reversedHalf.Next
        originalHead = originalHead.Next
    }

    return maxSum
}

func reverseLinkedList(head *ListNode) *ListNode {
    var headOfReversedList, currNode *ListNode = nil, head

    for currNode != nil {
        headOfReversedList, currNode, currNode.Next = currNode, currNode.Next, headOfReversedList
    }

    return headOfReversedList
}

func printLinkedList(l *ListNode) {
	for l != nil {
		fmt.Print(l.Val, " ")
		l = l.Next
	}
	fmt.Println()
}

func main() {
	l1 := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}
	fmt.Println(pairSumReverseListApproach(l1))
}


