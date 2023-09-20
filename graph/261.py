'''
#bfs, #dfs, #dsu, #tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an 
integer n and a list of edges where edges[i] = [ai, bi] indicates that 
there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and 
false otherwise.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
'''

import collections


class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node_1: int, node_2: int) -> int:
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 != root_node_2:
            if self.rank[root_node_1] < self.rank[root_node_2]:
                self.root[root_node_1] = root_node_2
                self.rank[root_node_2] += self.rank[root_node_1]
            else:
                self.root[root_node_2] = root_node_1
                self.rank[root_node_1] += self.rank[root_node_2]

    def is_connected(self, node_1: int, node_2: int) -> bool:
        return self.find(node_1) == self.find(node_2)
    
    def is_tree(self, n: int) -> bool:
        for node in range(n):
            self.find(node)
        
        return all(self.root[0] == e for e in self.root)


class Solution:

    def _dsu_approach(self, 
                            n: int, 
                            edges: list[list[int]]
                            ) -> bool:

        if len(edges) != n - 1:
            return False
        
        uf = UnionFind(n)

        for edge in edges:
            parent, child = edge
            if uf.is_connected(parent, child):
                return False
            uf.union(parent, child)

        return uf.is_tree(n)

    def _dfs_approach(self, 
                      n: int, 
                      edges: list[list[int]]
                      ) -> bool:

        if len(edges) != n - 1:
            return False
        
        visited = [False for _ in range(n)]
        adj_list = collections.defaultdict(list)
        for edge in edges:
            parent, child = edge
            adj_list[parent].append(child)
            adj_list[child].append(parent)
            
        def dfs(cur_node: int, prev_node: int) -> bool:
            if visited[cur_node]:
                return False
            
            visited[cur_node] = True
            
            for next_node in adj_list[cur_node]:
                if next_node == prev_node:
                    continue
                if not dfs(next_node, cur_node):
                    return False
                
            return True

        return dfs(0, 0) and visited.count(True) == n

    def _bfs_approach(self, 
                      n: int, 
                      edges: list[list[int]]
                      ) -> bool:

        if len(edges) != n - 1:
            return False
        
        visited = [False for _ in range(n)]
        adj_list = collections.defaultdict(list)
        for edge in edges:
            parent, child = edge
            adj_list[parent].append(child)
            adj_list[child].append(parent)

        queue = collections.deque()
        queue.append([0, 0])
        visited[0] = True
        
        while queue:
            cur_node, prev_node = queue.popleft()

            for next_node in adj_list[cur_node]:
                if next_node == prev_node:
                    continue
                if visited[next_node]:
                    return False
                visited[next_node] = True
                queue.append([next_node, cur_node])
        
        return visited.count(True) == n

    def valid_tree(self, 
                   n: int, 
                   edges: list[list[int]]
                   ) -> bool:
        return self._dfs_approach(n, edges)
        # return self._bfs_approach(n, edges)
        # return self._dsu_approach(n, edges)

sol = Solution()
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
print(sol.valid_tree(n, edges))
n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# n = 2
# edges = [[1,0]] 
# n = 3 
# edges = [[1,0],[2,0]]
# n = 1
# edges = []
n = 4
edges = [[0,1],[2,3],[1,2]]
print(sol.valid_tree(n, edges))