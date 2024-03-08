package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// time O(n log n) ~ O(n^2)
// space O(h): h = log n | n
func pathSum(root *TreeNode, targetSum int) int {
	counter := 0
	var summarize func(node *TreeNode, sum int)
	summarize = func(node *TreeNode, sum int) {
		if node == nil {
			return
		}
		sum += node.Val
		if sum == targetSum {
			counter++
		}

		summarize(node.Left, sum)
		summarize(node.Right, sum)
	}

	var traverse func(node *TreeNode)
	traverse = func(node *TreeNode) {
		if node == nil {
			return
		}

		summarize(node, 0)
		traverse(node.Left)
		traverse(node.Right)
	}

	traverse(root)
	return counter
}

func main() {
	root1 := &TreeNode{10,
		&TreeNode{5,
			&TreeNode{3,
				&TreeNode{3,
					nil,
					nil},
				&TreeNode{-2,
					nil,
					nil},
			},
			&TreeNode{2,
				nil,
				&TreeNode{1,
					nil,
					nil},
			},
		},
		&TreeNode{-3,
			nil,
			&TreeNode{11,
				nil,
				nil},
		},
	}
	fmt.Println(pathSum(root1, 8))
	root2 := &TreeNode{1,
		nil,
		&TreeNode{2,
			nil,
			&TreeNode{3,
				nil,
				&TreeNode{4,
					nil,
					&TreeNode{5,
						nil,
						nil},
				},
			},
		},
	}
	fmt.Println(pathSum(root2, 3))
}
