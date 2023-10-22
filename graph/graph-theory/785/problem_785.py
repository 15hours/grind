'''
#bfs, #dfs, #dsu

There is an undirected graph with n nodes, where each node is numbered 
between 0 and n - 1. You are given a 2D array graph, where graph[u] is 
an array of nodes that node u is adjacent to. More formally, for each v 
in graph[u], there is an undirected edge between node u and node v. The 
graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate 
values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v 
such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two 
independent sets A and B such that every edge in the graph connects a 
node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two 
independent sets such that every edge connects a node in one and a node 
in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and 
{1, 3}.
'''
import collections


class UnionFind:
    def __init__(self, graph: int) -> int:
        num_nodes = len(graph)
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

    def is_connected(self, node_1: int, node_2: int) -> bool:
        return self.find(node_1) == self.find(node_2)


class Solution:

    def dsu_approach(self, graph: list[list[int]]) -> bool:
        print("[DSU]")

        num_nodes = len(graph)
        uf = UnionFind(graph)

        for node in range(num_nodes):
            for next_node in graph[node]:
                if uf.is_connected(node, next_node):
                    return False
                uf.union(graph[node][0], next_node)

        return True

    def dfs_approach(self, graph: list[list[int]]) -> bool:
        print("[DFS]")
        graph_copy = [row[:] for row in graph]
        num_nodes = len(graph_copy)
        color = [0 for _ in range(num_nodes)]

        def dfs(cur_node: int, cur_color: int) -> bool:
            if color[cur_node] != 0:
                return color[cur_node] == cur_color

            color[cur_node] = cur_color
            next_color = -cur_color
            for next_node in graph_copy[cur_node]:
                if not dfs(next_node, next_color):
                    return False

            return True

        for node in range(num_nodes):
            if color[node] == 0 and not dfs(node, 1):
                return False

        return True

    def bfs_approach(self, graph: list[list[int]]) -> bool:
        print("[BFS]")

        graph_copy = [row[:] for row in graph]
        num_nodes = len(graph_copy)
        color = [0 for _ in range(num_nodes)]

        def bfs(start_node: int) -> bool:
            queue = collections.deque()
            start_color = 1
            queue.append([start_node, start_color])

        def bfs(start_node):
            queue = collections.deque()
            start_color = 1
            queue.append([start_node, start_color])
            color[start_node] = start_color

            while queue:
                cur_node, cur_color = queue.popleft()

                next_color = -cur_color
                for next_node in graph[cur_node]:
                    if color[next_node] == 0:
                        color[next_node] = next_color
                        queue.append([next_node, next_color])
                    elif color[next_node] == cur_color:
                        return False

            return True

        for node in range(num_nodes):
            if color[node] == 0 and not bfs(node):
                return False

        return True
