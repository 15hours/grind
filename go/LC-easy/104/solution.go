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

func maxDepth(root *TreeNode) int {
	// return bfsApproach(root)
	return conciseBfsApproach(root)
	// return dfsApproach(root)
	// return conciseDfsApproach(root)
}

type QueueElement struct {
	Node  *TreeNode
	Depth int
}

func bfsApproach(root *TreeNode) int {
	if root == nil {
		return 0
	}

	var maxDepth int
	var queue []QueueElement

	queue = append(queue, QueueElement{Node: root, Depth: 1})

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]

		maxDepth = max(maxDepth, curr.Depth)

		if curr.Node.Left != nil {
			newNode := curr.Node.Left
			newDepth := curr.Depth + 1
			queue = append(queue, QueueElement{Node: newNode, Depth: newDepth})
		}
		if curr.Node.Right != nil {
			newNode := curr.Node.Right
			newDepth := curr.Depth + 1
			queue = append(queue, QueueElement{Node: newNode, Depth: newDepth})
		}
	}

	return maxDepth
}

func conciseBfsApproach(root *TreeNode) int {
	if root == nil {
		return 0
	}

	var depthLevel int
	queue := list.New()

	queue.PushBack(root)

	for queue.Len() > 0 {
		currentLevelElements := queue.Len()
		for i := 0; i < currentLevelElements; i++ {
			queueElement := queue.Front()
			queue.Remove(queueElement)
			currNode := queueElement.Value.(*TreeNode)

			if currNode.Left != nil {
				queue.PushBack(currNode.Left)
			}
			if currNode.Right != nil {
				queue.PushBack(currNode.Right)
			}
		}

		depthLevel++
	}

	return depthLevel
}

func dfsApproach(root *TreeNode) int {
	if root == nil {
		return 0
	}

	var traverse func(node *TreeNode, depth int) int
	traverse = func(node *TreeNode, depth int) int {
		if node == nil {
			return depth
		}

		leftDepth := traverse(node.Left, depth+1)
		rightDepth := traverse(node.Right, depth+1)

		return max(leftDepth, rightDepth)
	}

	return traverse(root, 0)
}

func conciseDfsApproach(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return max(conciseDfsApproach(root.Left), conciseDfsApproach(root.Right)) + 1
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

	fmt.Println(maxDepth(root))
}
