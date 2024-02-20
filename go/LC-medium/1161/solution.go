package main

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

// time O(n)
// space O(n)
func maxLevelSumBFSApproach(root *TreeNode) int {
    queue := []*TreeNode{}
    queue = append(queue, root)
    maxSum := root.Val
    idx := 1
    layerCount := 1

    for len(queue) != 0 {
        curLayer := queue
        queue = []*TreeNode{}

        curSum := 0
        for _, node := range curLayer {
            curSum += node.Val

            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }

        if curSum > maxSum {
            maxSum = curSum
            idx = layerCount
        }

        layerCount++
    }

    return idx
}

// time O(n)
// space O(n)
func maxLevelSumDFSApproach(root *TreeNode) int {
    layerSums := []int{}

    var traverse func(node *TreeNode, curLayer int)
    traverse = func(node *TreeNode, curLayer int) {
        if node == nil {
            return
        }

        if len(layerSums) < curLayer {
            layerSums = append(layerSums, node.Val)
        } else {
            layerSums[curLayer - 1] += node.Val
        }

        traverse(node.Left, curLayer + 1)
        traverse(node.Right, curLayer + 1)
    }

    traverse(root, 1)

    maxSum := layerSums[0]
    idx := 0
    for i, s := range layerSums {
        if s > maxSum {
            maxSum = s
            idx = i
        }
    }

    return idx
}
