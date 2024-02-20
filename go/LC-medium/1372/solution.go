package main

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

// time O(log n) ~ O(n)
// space O(h): O(log n) | O(n)
func longestZigZag(root *TreeNode) int {
    maxLenPath := 0
    var traverse func(node *TreeNode, dir int, lenPath int)
    traverse = func(node *TreeNode, dir int, lenPath int) {
        if node == nil {
            return
        }
        maxLenPath = max(maxLenPath, lenPath)

        if dir == -1 {
            traverse(node.Right, 1, lenPath + 1)
            traverse(node.Left, -1, 1)
        } else {
            traverse(node.Left, -1, lenPath + 1)
            traverse(node.Right, 1, 1)
        }
    }

    traverse(root.Left, -1, 1)
    traverse(root.Right, 1, 1)
    return maxLenPath
}


func longestZigZagConciseDFSApproach(root *TreeNode) int {
    var traverse func(node *TreeNode, dir int, lenPath int) int
    traverse = func(node *TreeNode, dir int, lenPath int) int {
        if node == nil {
            return lenPath
        }

        if dir == -1 {
            return max(traverse(node.Right, 1, lenPath + 1), traverse(node.Left, -1, 0))
        }

        return max(traverse(node.Left, -1, lenPath + 1), traverse(node.Right, 1, 0))
    }

    return max(traverse(root.Left, -1, 0), traverse(root.Right, 1, 0))
}
