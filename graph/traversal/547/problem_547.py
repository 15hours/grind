'''
#bfs, #dfs, #dsu

There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected 
directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and 
no other cities outside of the group.

You are given an n x n matrix is_connected where is_connected[i][j] = 1 
if the ith city and the jth city are directly connected, 
and is_connected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: is_connected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
'''
import collections


class UnionFind:
    def __init__(self, num_nodes: int) -> None:
        self.root = list(range(num_nodes))
        self.rank = [1 for _ in range(num_nodes)]

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node_1: int, node_2: int) -> None:
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 != root_node_2:
            if self.rank[root_node_1] < self.rank[root_node_2]:
                self.root[root_node_1] = root_node_2
                self.rank[root_node_2] += self.rank[root_node_1]
            else:
                self.root[root_node_2] = root_node_1
                self.rank[root_node_1] += self.rank[root_node_2]


class Solution(object):

    def dsu_approach(self, is_connected: list[list[int]]) -> int:
        print("[DSU]")

        num_nodes = len(is_connected)
        uf = UnionFind(num_nodes)

        for node_1 in range(num_nodes):
            for node_2 in range(node_1, num_nodes):
                if is_connected[node_1][node_2] == 1:
                    uf.union(node_1, node_2)

        root = [uf.find(node) for node in range(num_nodes)]
        return len(set(root))

    def dfs_approach(self, is_connected: list[list[int]]) -> None:
        print("[DFS]")

        num_nodes = len(is_connected)
        visited = [False for _ in range(num_nodes)]

        def dfs(cur_node: int) -> None:
            for next_node, is_neighbor in enumerate(is_connected[cur_node]):
                if not visited[next_node] and is_neighbor:
                    visited[next_node] = True
                    dfs(next_node)

        num_components = 0
        for node in range(num_nodes):
            if not visited[node]:
                visited[node] = True
                num_components += 1
                dfs(node)

        return num_components

    def bfs_approach(self, is_connected: list[list[int]]) -> None:
        print("[BFS]")

        num_nodes = len(is_connected)
        visited = [False for _ in range(num_nodes)]

        def bfs(start_node: int) -> None:
            queue = collections.deque()
            queue.append(start_node)

            while queue:
                cur_node = queue.popleft()

                for next_node, neighbor in enumerate(is_connected[cur_node]):
                    if not visited[next_node] and neighbor:
                        visited[next_node] = True

                        queue.append(next_node)

        num_components = 0
        for node in range(num_nodes):
            if not visited[node]:
                visited[node] = True
                num_components += 1
                bfs(node)

        return num_components
