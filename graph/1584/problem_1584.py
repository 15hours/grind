import collections
import heapq


class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))
        self.rank = [1] * n
        
    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node_1, node_2):
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 == root_node_2:
            return False
        
        if self.rank[root_node_1] < self.rank[root_node_2]:
            self.root[root_node_1] = root_node_2
        elif self.rank[root_node_2] < self.rank[root_node_1]:
            self.root[root_node_2] = root_node_1
        else:
            self.root[root_node_2] = root_node_1
            self.rank[root_node_1] += 1

        return True


class Solution:

    def kruskal_approach(self, points: list[list[int]]) -> int:
        print("[Kruskal]")
        print("space complexity: O(E)")
        print("time complexity: O(E*logE)")
        
        num_nodes = len(points)
        pq = []
        for i in range(num_nodes - 1):
            x1, y1 = points[i]
            for j in range(i + 1, num_nodes):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                pq.append([weight, i, j])

        heapq.heapify(pq)
        uf = UnionFind(num_nodes)
        
        connected_nodes_count = num_nodes - 1
        cost = 0
        while pq and connected_nodes_count > 0:
            weight, node_1, node_2 = heapq.heappop(pq)
            if uf.union(node_1, node_2):
                cost += weight
                connected_nodes_count -= 1

        return cost
#TODO: implement Prim's algorithm    