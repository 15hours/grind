package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// time O(h)
// space O(h)
func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val < key {
		root.Right = deleteNode(root.Right, key)
	} else if root.Val > key {
		root.Left = deleteNode(root.Left, key)
	} else {
		if root.Left == nil {
			return root.Right
		} else if root.Right == nil {
			return root.Left
		} else {
			successor := subtreeMinimum(root.Right)

			leftSubTree := root.Left
			rightSubTree := deleteNode(root.Right, successor.Val)

			successor.Left = leftSubTree
			successor.Right = rightSubTree

			return successor
		}
	}

	return root
}

// time O(h)
// space O(1)
func subtreeMinimum(node *TreeNode) *TreeNode {
	for node.Left != nil {
		node = node.Left
	}
	return node
}
