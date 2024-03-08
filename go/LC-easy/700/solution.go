package main

import (
	"container/list"
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	// return bfsApproach1(root, val)
	// return bfsApproach2(root, val)
	return dfsTraverse(root, val)
}

func bfsApproach1(root *TreeNode, val int) *TreeNode {
	if root.Val == val {
		return root
	}

	var queue []TreeNode
	queue = append(queue, *root)

	for len(queue) > 0 {
		currNode := queue[0]
		queue = queue[1:]

		if currNode.Left != nil {
			if currNode.Left.Val == val {
				return currNode.Left
			}
			queue = append(queue, *currNode.Left)
		}
		if currNode.Right != nil {
			if currNode.Right.Val == val {
				return currNode.Right
			}
			queue = append(queue, *currNode.Right)
		}
	}

	return nil
}

func bfsApproach2(root *TreeNode, val int) *TreeNode {
	if root.Val == val {
		return root
	}

	queue := list.New()
	queue.PushBack(root)

	for queue.Len() > 0 {
		currentLevelElements := queue.Len()
		for i := 0; i < currentLevelElements; i++ {
			queueElement := queue.Front()
			queue.Remove(queueElement)
			currNode := queueElement.Value.(*TreeNode)

			if currNode.Left != nil {
				if currNode.Left.Val == val {
					return currNode.Left
				}
				queue.PushBack(currNode.Left)
			}
			if currNode.Right != nil {
				if currNode.Right.Val == val {
					return currNode.Right
				}
				queue.PushBack(currNode.Right)
			}
		}
	}

	return nil
}

func dfsTraverse(node *TreeNode, val int) *TreeNode {
	if node == nil {
		return nil
	}

	if node.Val == val {
		return node
	}

	var nextNode *TreeNode
	if node.Val > val {
		nextNode = dfsTraverse(node.Left, val)
	}
	if node.Val < val {
		nextNode = dfsTraverse(node.Right, val)
	}

	return nextNode
}

func main() {
	root := &TreeNode{
		Val: 5,
		Left: &TreeNode{
			Val: 3,
			Left: &TreeNode{
				Val:   1,
				Left:  nil,
				Right: nil,
			},
			Right: &TreeNode{
				Val:  4,
				Left: nil,
				Right: &TreeNode{
					Val:   10,
					Left:  nil,
					Right: nil,
				},
			},
		},
		Right: &TreeNode{
			Val:  7,
			Left: nil,
			Right: &TreeNode{
				Val:   9,
				Left:  nil,
				Right: nil,
			},
		},
	}

	fmt.Println(searchBST(root, 3))
}
