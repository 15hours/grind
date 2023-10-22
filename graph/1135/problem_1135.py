'''
#mst, #kruskal, #prim

There are n cities labeled from 1 to n. You are given the integer n and
an array connections where connections[i] = [xi, yi, costi] indicates
that the cost of connecting city xi and city yi (bidirectional
connection) is costi.

Return the minimum cost to connect all the n cities such that there is
at least one path between each pair of cities. If it is impossible to
connect all the n cities, return -1,

The cost is the sum of the connections' costs used.
 

Example 1:

Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]

Output: 6

Explanation: Choosing any 2 edges will connect all cities so we choose
the minimum 2.


Example 2:

Input: n = 4, connections = [[1,2,3],[3,4,4]]

Output: -1

Explanation: There is no way to connect all cities even if all edges are
used.
'''
import collections
import heapq


class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node_1: int, node_2: int) -> bool:
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

    def kruskal_approach(self, n: int, connections: list[list[int]]) -> int:
        print("[Kruskal]")
        print("space complexity: O(V)")
        print("time complexity: O(E*logE)")

        if len(connections) < n - 1:
            return -1

        sorted_connections = sorted(connections, key=lambda x: x[2])
        uf = UnionFind(n + 1)
        
        used_edges = 0
        mst_cost = 0
        for node_1, node_2, weight in sorted_connections:
            if uf.union(node_1, node_2):
                used_edges += 1
                mst_cost += weight
            
            if used_edges == n - 1:
                return mst_cost
        
        return -1
    
    def prim_approach(self, n: int, connections: list[list[int]]) -> int:
        print("[Prim]")
        print("space complexity: O(V)")
        print("time complexity: O(E*logE)")
        
        if len(connections) < n - 1:
            return -1
        adj_list = collections.defaultdict(list)
        
        for node_1, node_2, weight in connections:
            adj_list[node_1].append([node_2, weight])
            adj_list[node_2].append([node_1, weight])

        vis = []
        pq = []
        mst_cost = 0
        in_mst = [False] * (n + 1)

        vis.append(n)
        in_mst[n] = True

        for _ in range(n - 1):
            cur_node = vis[-1]
            if not adj_list[cur_node]:
                return -1
            for next_node, weight in adj_list[cur_node]:
                if in_mst[next_node]:
                    continue
                heapq.heappush(pq, [weight, next_node])
            
            while pq:
                weight, chosen_node = heapq.heappop(pq)
                if not in_mst[chosen_node]:
                    mst_cost += weight
                    vis.append(chosen_node)
                    in_mst[chosen_node] = True
                    break
            else:
                return -1

        return mst_cost