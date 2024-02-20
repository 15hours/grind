package main

type ListNode struct {
    Val int
    Next *ListNode
}

func deleteMiddle(head *ListNode) *ListNode {
    curNode := head
    numNodes := 0
    for curNode != nil {
        numNodes++
        curNode = curNode.Next
    }

    if numNodes == 1 {
        return nil
    }

    newList := head
    idx := 0
    for newList != nil && newList.Next != nil {
        if numNodes / 2 == idx + 1 {
            newList.Next = newList.Next.Next
            break
        }

        newList = newList.Next
        idx++
    }

    return head
}

// Using slow and fast pointers 
func deleteMiddleTwoPointersApproach(head *ListNode) *ListNode {
    if head.Next == nil {
        return nil
    }
    slow := head
    fast := head.Next.Next

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    slow.Next = slow.Next.Next

    return head
}
