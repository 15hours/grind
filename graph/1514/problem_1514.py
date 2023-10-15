'''
#dijkstra, #bf, #spfa

You are given an undirected weighted graph of n nodes (0-indexed),
represented by an edge list where edges[i] = [a, b] is an undirected
edge connecting the nodes a and b with a probability of success of
traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum
probability of success to go from start to end and return its success
probability.

If there is no path from start to end, return 0. Your answer will be
accepted if it differs from the correct answer by at most 1e-5.
 

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2],
start = 0, end = 2

Output: 0.25000

Explanation: There are two paths from start to end, one having a
probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.


Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3],
start = 0, end = 2

Output: 0.30000


Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2

Output: 0.00000

Explanation: There is no path between 0 and 2.
'''
import collections
import heapq


class Solution:

    def dijkstra_approach(self,
                          n: int,
                          edges: list[list[int]],
                          succ_prob: list[float],
                          start_node: int,
                          end_node: int
                          ) -> float:
        print("[Dijkstra]")
        print("space complexity: O(E+V)")
        print("time complexity: O(V+E*logV)")

        adj_list = collections.defaultdict(list)
        for [node_1, node_2], cost in zip(edges, succ_prob):
            adj_list[node_1].append([node_2, -cost])
            adj_list[node_2].append([node_1, -cost])

        pq = []
        start_cost = -1 
        heapq.heappush(pq, [start_cost, start_node])

        costs = [0] * n
        costs[start_node] = -1

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if cur_node == end_node:
                return -cur_cost
            
            for next_node, cost in adj_list[cur_node]:
                new_cost = -cur_cost * cost
                if new_cost < costs[next_node]:
                    costs[next_node] = new_cost
                    heapq.heappush(pq, [new_cost, next_node]) 
                    
        return 0

    def bf_with_two_arrays_approach(self,
                                    n: int,
                                    edges: list[list[int]],
                                    succ_prob: list[float],
                                    start_node: int,
                                    end_node: int
                                    ) -> float:
        print("[BF with 2 arrays]")
        print("space complexity: O(V)")
        print("time complexity: O(V*(E+V))")
            
        prev_state = [0] * n
        prev_state[start_node] = 1 
        cur_state = prev_state[:]
        
        for _ in range(1, n):
            changed = False
            cur_state[start_node] = 1
            
            for [node_1, node_2], cost in zip(edges, succ_prob):
                new_cost_1 = prev_state[node_2] * cost
                new_cost_2 = prev_state[node_1] * cost

                if new_cost_1 > prev_state[node_1]:
                    cur_state[node_1] = new_cost_1
                    changed = True
                if new_cost_2 > prev_state[node_2]:
                    cur_state[node_2] = new_cost_2
                    changed = True
                    
            if not changed:
                break
            
            prev_state = cur_state[:]
                   
        return cur_state[end_node]
    
    def bf_with_one_array_approach(self,
                                   n: int,
                                   edges: list[list[int]],
                                   succ_prob: list[float],
                                   start_node: int,
                                   end_node: int
                                   ) -> float:
        print("[BF with one array]")
        print("space complexity: O(V)")
        print("time complexity: O(V*E)")
        
        costs = [0] * n
        costs[start_node] = 1
        
        for i in range(n):
            changed = False

            for j in range(len(edges)):
                node_1, node_2 = edges[j]
                edge_cost = succ_prob[j]
                
                new_cost_node_2 = costs[node_1] * edge_cost
                if new_cost_node_2 > costs[node_2]:
                    costs[node_2] = new_cost_node_2
                    changed = True

                new_cost_node_1 = costs[node_2] * edge_cost
                if new_cost_node_1 > costs[node_1]:
                    costs[node_1] = new_cost_node_1
                    changed = True
                
            if not changed:
                break

        return costs[end_node]
                     
    def spfa_approach(self,
                      n: int,
                      edges: list[list[int]],
                      succ_prob: list[float],
                      start_node: int,
                      end_node: int
                      ) -> float:
        print("[SPFA]")
        print("space complexity: O(E+V)")
        print("time complexity: O(V*E)")

        adj_list = collections.defaultdict(list)
        for [node_1, node_2], cost in zip(edges, succ_prob):
            adj_list[node_1].append([node_2, -cost])
            adj_list[node_2].append([node_1, -cost])

        queue = collections.deque()
        queue.append(start_node)
        
        costs = [0] * n
        costs[start_node] = -1

        while queue:
            cur_node = queue.popleft()

            for next_node, cost in adj_list[cur_node]:
                
                new_cost = -costs[cur_node] * cost
                if new_cost < costs[next_node]:
                    costs[next_node] = new_cost
                    queue.append(next_node)

        return -costs[end_node]