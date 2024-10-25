package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// time O(n)
// space O(n)
func rightSideViewBFSApproach(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	queue := []*TreeNode{}
	queue = append(queue, root)
	result := []int{}
	result = append(result, queue[0].Val)

	for len(queue) != 0 {
		layer := queue
		queue = []*TreeNode{}

		for _, node := range layer {
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		if len(queue) != 0 {
			result = append(result, queue[len(queue)-1].Val)
		}
	}

	return result
}

func rightSideViewDFSApproach(root *TreeNode) []int {
	result := []int{}

	var traverse func(node *TreeNode, depth int)
	traverse = func(node *TreeNode, depth int) {
		if node == nil {
			return
		}

		if len(result) == depth {
			result = append(result, node.Val)
		}

		traverse(node.Right, depth+1)
		traverse(node.Left, depth+1)
	}

	traverse(root, 0)
	return result
}

func main() {
	root := &TreeNode{1,
		&TreeNode{2,
			nil,
			&TreeNode{5,
				nil,
				nil},
		},
		&TreeNode{3,
			nil,
			&TreeNode{4,
				nil,
				nil},
		},
	}

	rightSideViewBFSApproach(root)
	rightSideViewDFSApproach(root)
}
