'''
#dp, #bf, #bfs, #dijkstra

There are n cities connected by some number of flights. You are given an
array flights where flights[i] = [fromi, toi, pricei] indicates that
there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest
price from src to dst with at most k stops. If there is no such route,
return -1.
 

Example 1:

Input: n = 4, flights =
[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k
= 1

Output: 700

Explanation: The graph is shown above. The optimal path with at most 1
stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid
because it uses 2 stops.


Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst =
2, k = 1

Output: 200

Explanation: The graph is shown above. The optimal path with at most 1
stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.


Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst =
2, k = 0

Output: 500

Explanation: The graph is shown above. The optimal path with no stops
from city 0 to 2 is marked in red and has cost 500.
'''

import collections
import math
import heapq


class Solution:

    def dp_approach(self,
                    n: int,
                    flights: list[list[int]],
                    src: int,
                    dst: int,
                    k: int
                    ) -> int:
        print("[DP]")

        adj_list_rev = collections.defaultdict(list)
        edge_cost = collections.defaultdict(int)
        shortest_distance = [[math.inf for _ in range(n)]
                             for _ in range(k + 2)]
        shortest_distance[0][src] = 0

        for parent, node, cost in flights:
            adj_list_rev[node].append(parent)
            edge_cost[(parent, node)] = cost

        for edge_num in range(1, len(shortest_distance)):
            shortest_distance[edge_num][src] = 0
            for node in range(n):
                for prev_node in adj_list_rev[node]:
                    if shortest_distance[edge_num - 1][prev_node] == math.inf:
                        continue

                    new_cost = shortest_distance[edge_num - 1][prev_node] \
                        + edge_cost[(prev_node, node)]
                    if new_cost < shortest_distance[edge_num][node]:
                        shortest_distance[edge_num][node] = new_cost

        answer = shortest_distance[k + 1][dst]
        return answer if answer != math.inf else -1

    def bf_with_two_arrays(self,
                           n: int,
                           flights: list[list[int]],
                           src: int,
                           dst: int,
                           k: int
                           ) -> int:
        print("[BF with two arrays]")

        prev_state = [math.inf] * n
        cur_state = [math.inf] * n
        prev_state[src] = 0

        for _ in range(1, k + 2):
            cur_state[src] = 0
            for flight in flights:
                prev_node, node, cost = flight

                if prev_state[prev_node] < math.inf:
                    cur_state[node] = min(cur_state[node],
                                          prev_state[prev_node] + cost)

            prev_state = cur_state.copy()

        answer = prev_state[dst]
        return answer if answer != math.inf else -1

    def bfs_approach(self,
                     n: int,
                     flights: list[list[int]],
                     src: int,
                     dst: int,
                     k: int
                     ) -> int:
        print("[BFS]")

        adj_list = collections.defaultdict(list)
        edge_cost = collections.defaultdict(int)

        for flight in flights:
            parent, node, cost = flight

            adj_list[parent].append(node)
            edge_cost[(parent, node)] = cost

        queue = collections.deque()
        start_steps, start_cost = 0, 0
        queue.append([src, start_steps, start_cost])
        dists = [math.inf] * n
        dists[src] = 0

        while queue:
            cur_node, steps, cost = queue.popleft()

            for next_node in adj_list[cur_node]:
                if steps + 1 <= k + 1:
                    new_cost = cost + edge_cost[(cur_node, next_node)]
                    if next_node == dst:
                        if new_cost < dists[next_node]:
                            dists[next_node] = new_cost
                    else:
                        if steps + 1 == k + 1:
                            continue
                        if new_cost < dists[next_node]:
                            dists[next_node] = new_cost
                            queue.append([next_node, steps + 1, new_cost])

        answer = dists[dst]
        if answer != math.inf:
            return answer
        return -1

    def dijkstra_approach(self,
                          n: int,
                          flights: list[list[int]],
                          src: int,
                          dst: int,
                          k: int
                          ) -> int:
        print("[Dijkstra's algorithm]")

        adj_list = collections.defaultdict(list)
        for parent, node, cost in flights:
            adj_list[parent].append([node, cost])

        stops = [math.inf] * n
        pq = []
        start_cost, start_steps = 0, 0
        heapq.heappush(pq, [start_cost, src, start_steps])

        while pq:
            cur_cost, cur_node, cur_steps = heapq.heappop(pq)

            if cur_steps > stops[cur_node] or cur_steps > k + 1:
                continue

            if cur_node == dst:
                return cur_cost

            stops[cur_node] = cur_steps
            for next_node, next_cost in adj_list[cur_node]:
                heapq.heappush(pq, [next_cost + cur_cost, next_node,
                                    cur_steps + 1])

        return -1
