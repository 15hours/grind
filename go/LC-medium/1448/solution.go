package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type queueElement struct {
	Node   *TreeNode
	maxVal int
}

func goodNodesBFSApproach(root *TreeNode) int {
	queue := make([]queueElement, 0)
	queue = append(queue, queueElement{Node: root, maxVal: root.Val})

	counter := 0
	for len(queue) != 0 {
		curNode, curMaxVal := queue[0].Node, queue[0].maxVal
		queue = queue[1:]

		if curNode == nil {
			continue
		}

		if curNode.Val >= curMaxVal {
			curMaxVal = curNode.Val
			counter++
		}

		queue = append(queue, queueElement{Node: curNode.Left, maxVal: curMaxVal})
		queue = append(queue, queueElement{Node: curNode.Right, maxVal: curMaxVal})
	}

	return counter
}

func goodNodesDFSApproach(root *TreeNode) int {
	var traverse func(node *TreeNode, curMaxVal int) int
	traverse = func(node *TreeNode, curMaxVal int) int {
		if node == nil {
			return 0
		}

		count := 0
		if node.Val >= curMaxVal {
			curMaxVal = node.Val
			count = 1
		}

		return count + traverse(node.Left, curMaxVal) + traverse(node.Right, curMaxVal)
	}

	return traverse(root, root.Val)
}

func main() {
	root := &TreeNode{3,
		&TreeNode{1,
			&TreeNode{3, nil, nil},
			nil},
		&TreeNode{4,
			&TreeNode{1, nil, nil},
			&TreeNode{5, nil, nil}}}
	fmt.Println(goodNodesBFSApproach(root))
	fmt.Println(goodNodesDFSApproach(root))
}
