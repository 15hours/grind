'''
#mst, #kruskal, #prim

You are given an array points representing integer coordinates of some
points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
absolute value of val.

Return the minimum cost to make all points connected. All points are
connected if there is exactly one simple path between any two points.
 

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

Output: 20

Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.


Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]

Output: 18
        '''
import collections
import heapq
import math


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
        print("space complexity: O(V^2)")
        print("time complexity: O(V^2 * logV)")
        
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
        mst_cost = 0
        while pq and connected_nodes_count > 0:
            weight, node_1, node_2 = heapq.heappop(pq)
            if uf.union(node_1, node_2):
                mst_cost += weight
                connected_nodes_count -= 1

        return mst_cost
    
    def prim_approach(self, points: list[list[int]]) -> int:
        print("[Prim]")
        print("space complexity: O(V^2)")
        print("time complexity: O(V^2 * logV)")
        
        num_nodes = len(points)
        in_mst = [False] * num_nodes
        pq = []
        mst_cost = 0

        cur_node = 0
        for _ in range(num_nodes - 1):
            x1, y1 = points[cur_node]
            in_mst[cur_node] = True

            for next_node in range(num_nodes):
                if in_mst[next_node]:
                    continue
                x2, y2 = points[next_node]
                weight = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(pq, [weight, next_node])
                
            while pq:
                weight, next_node = heapq.heappop(pq)
                if not in_mst[next_node]:
                    mst_cost += weight
                    cur_node = next_node
                    break
       
        return mst_cost

    def opt_prim_approach(self, points: list[list[int]]) -> int:
        print("[Optimized Prim]")
        print("space complexity: O(V)")
        print("time complexity: O(V^2)")
        
        num_nodes = len(points)
        in_mst = [False] * num_nodes
        min_dist = [math.inf] * num_nodes
        mst_cost = 0
        
        start_node = 0
        min_dist[start_node] = 0

        for _ in range(num_nodes):
            cur_node = None
            cur_weight = math.inf
            for node in range(num_nodes):
                if not in_mst[node] and min_dist[node] < cur_weight:
                    cur_node = node
                    cur_weight = min_dist[node]
                    
            mst_cost += cur_weight
            in_mst[cur_node] = True
            
            x1, y1 = points[cur_node]
            for next_node in range(num_nodes):
                if in_mst[next_node]:
                    continue

                x2, y2 = points[next_node]
                weight = abs(x1 - x2) + abs(y1 - y2)
                if weight < min_dist[next_node]:
                    min_dist[next_node] = weight

        return mst_cost