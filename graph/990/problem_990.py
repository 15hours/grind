'''
#dfs, #dsu, #coloring

You are given an array of strings equations that represent 
relationships between variables where each string equations[i] is of 
length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that 
represent one-letter variable names.

Return true if it is possible to assign integers to variable names so 
as to satisfy all the given equations, or false otherwise.

Example 1:
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation 
is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
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
            if self.rank[root_node_2] <= self.rank[root_node_1]:
                self.root[root_node_2] = root_node_1
                self.rank[root_node_1] += self.rank[root_node_2]
            else:
                self.root[root_node_1] = root_node_2
                self.rank[root_node_2] += self.rank[root_node_1]

    def same_root(self, node_1: int, node_2: int) -> bool:
        return self.find(self.root[node_1]) == self.find(self.root[node_2])


class Solution:

    def dsu_approach(self, equations: list[str]) -> bool:
        print("[DSU]")
        uf = UnionFind(26)
        not_equal = []
        for equation in equations:
            x, sign, _, y = equation

            node_1, node_2 = ord(x) - ord('a'), ord(y) - ord('a')
            if sign == "=" and node_1 != node_2:
                uf.union(node_1, node_2)
            if sign == "!":
                not_equal.append([node_1, node_2])
        
        for node_1, node_2 in not_equal:
            if uf.find(node_1) == uf.find(node_2):
                return False
            
        return True

    def dfs_approach(self, equations: list[str]) -> bool:
        print("[DFS]")
        adj_list = collections.defaultdict(list)
        not_equal = []
        for equation in equations:
            x, sign, _, y = equation

            node_1, node_2 = ord(x) - ord('a'), ord(y) - ord('a')
            if sign == "=" and node_1 != node_2:
                adj_list[node_1].append(node_2)
                adj_list[node_2].append(node_1)
            if sign == "!":
                not_equal.append([node_1, node_2])
        
        color = [-1 for _ in range(26)]
        def dfs(cur_node: int, graph_color: int) -> None:
            if color[cur_node] == -1:
                color[cur_node] = graph_color
                for next_node in adj_list[cur_node]:
                    dfs(next_node, graph_color)

        for node in range(26):
            if color[node] == -1:
                graph_color = node
                dfs(node, graph_color)
        
        for node_1, node_2 in not_equal:
            if color[node_1] == color[node_2]:
                return False
            
        return True