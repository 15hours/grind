'''
#bfs, #dfs

Given the root of a binary tree, the value of a target node target, and 
an integer k, return an array of the values of all nodes that have a 
distance k from the target node.

You can return the answer in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with 
value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []
'''
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def get_graph_dfs(self, cur_node: TreeNode) -> dict[list[int]]:
        graph = collections.defaultdict(list)
        parent = None

        def dfs(cur_node: TreeNode, parent: TreeNode):
            nonlocal graph
            if cur_node is None:
                return

            if parent is not None:
                graph[cur_node.val].append(parent.val)
            if cur_node.left is not None:
                graph[cur_node.val].append(cur_node.left.val)
            if cur_node.right is not None:
                graph[cur_node.val].append(cur_node.right.val)

            dfs(cur_node.left, cur_node)
            dfs(cur_node.right, cur_node)

        dfs(cur_node, parent)
        return graph

    def get_answer_dfs(self,
                       graph: dict[list[int]],
                       target: TreeNode,
                       k: int
                       ) -> list[int]:

        answer = []
        steps = 0
        visited = [False for _ in range(len(graph))]
        visited[target.val] = True

        def dfs(cur_node, steps):
            nonlocal answer

            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    if steps + 1 == k:
                        answer.append(next_node)
                    else:
                        dfs(next_node, steps + 1)

        dfs(target.val, steps)
        return answer

    def get_graph_bfs(self, cur_node: TreeNode) -> dict[list[int]]:
        graph = collections.defaultdict(list)
        queue = collections.deque()
        queue.append(cur_node)

        while queue:
            cur_node = queue.popleft()

            if cur_node.left is not None:
                graph[cur_node.left.val].append(cur_node.val)
                graph[cur_node.val].append(cur_node.left.val)
                queue.append(cur_node.left)
            if cur_node.right is not None:
                graph[cur_node.right.val].append(cur_node.val)
                graph[cur_node.val].append(cur_node.right.val)
                queue.append(cur_node.right)

        return graph

    def get_answer_bfs(self,
                       graph: dict[list[int]],
                       target: TreeNode,
                       k: int
                       ) -> list[int]:

        queue = collections.deque()
        visited = [False for _ in range(len(graph))]
        answer = []

        visited[target.val] = True
        queue.append([target.val, 0])

        while queue:
            cur_node, steps = queue.popleft()

            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    if steps + 1 == k:
                        answer.append(next_node)
                    else:
                        queue.append([next_node, steps + 1])
        return answer

    def distance_k(self,
                   root: TreeNode,
                   target: TreeNode,
                   k: int
                   ) -> list[int]:
        if k == 0:
            return [target.val]

        # graph = self.get_graph_bfs(root)
        graph = self.get_graph_dfs(root)
        if len(graph) < target.val:
            return []

        # return self.get_answer_bfs(graph, target, k)
        return self.get_answer_dfs(graph, target, k)
