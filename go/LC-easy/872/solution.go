package main

import (
	"fmt"
	"slices"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	leafSequence1, leafSequence2 := []int{}, []int{}

	dfsTraverse(root1, &leafSequence1)
	dfsTraverse(root2, &leafSequence2)

	return slices.Equal(leafSequence1, leafSequence2)
}

func dfsTraverse(node *TreeNode, leafSequence *[]int) {
	if node == nil {
		return
	}

	if node.Left == nil && node.Right == nil {
		*leafSequence = append(*leafSequence, node.Val)
		return
	}

	dfsTraverse(node.Left, leafSequence)
	dfsTraverse(node.Right, leafSequence)
}

func main() {
	root1 := &TreeNode{
		Val: 3,
		Left: &TreeNode{
			Val:  5,
			Left: &TreeNode{Val: 6},
			Right: &TreeNode{
				Val:   2,
				Left:  &TreeNode{Val: 7},
				Right: &TreeNode{Val: 4},
			},
		},
		Right: &TreeNode{
			Val:   1,
			Left:  &TreeNode{Val: 9},
			Right: &TreeNode{Val: 8},
		},
	}
	root2 := &TreeNode{
		Val: 3,
		Left: &TreeNode{
			Val:  5,
			Left: &TreeNode{Val: 6},
			Right: &TreeNode{
				Val:   2,
				Left:  &TreeNode{Val: 7},
				Right: &TreeNode{Val: 4},
			},
		},
		Right: &TreeNode{
			Val:   1,
			Left:  &TreeNode{Val: 9},
			Right: &TreeNode{Val: 8},
		},
	}
	fmt.Println(leafSimilar(root1, root2))
}
