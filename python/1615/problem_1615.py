'''
#outdegree

There is an infrastructure of n cities with some number of roads 
connecting these cities. Each roads[i] = [ai, bi] indicates that there 
is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number 
of directly connected roads to either city. If a road is directly 
connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network 
rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network 
rank of the entire infrastructure.

Example 1:
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 
roads that are connected to either 0 or 1. The road between 0 and 1 is 
only counted once.

Example 2:
Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.

Example 3:
Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the 
cities do not have to be connected.
'''
import collections


class Solution:

    def _create_adj_dict(self,
                         n: int,
                         roads: list[list[int]]
                         ) -> [dict[list[int]], list[int]]:

        adj_dict = collections.defaultdict(list)
        outdegree = [0 for _ in range(n)]

        for edge in roads:
            node_1, node_2 = edge

            outdegree[node_1] += 1
            outdegree[node_2] += 1

            adj_dict[node_1].append(node_2)
            adj_dict[node_2].append(node_1)

        return adj_dict, outdegree

    def maximal_network_rank(self,
                             n: int,
                             roads: list[list[int]]
                             ) -> int:

        adj_dict, outdegree = self._create_adj_dict(n, roads)
        max_rank = 0

        for node_1 in range(n - 1):
            for node_2 in range(node_1 + 1, n):
                rank = outdegree[node_1] + outdegree[node_2]
                if node_1 in adj_dict[node_2]:
                    rank -= 1

                if rank > max_rank:
                    max_rank = rank

        return max_rank
