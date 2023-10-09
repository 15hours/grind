import collections
import math


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

    def basic_bf_approach(self,
                            n: int,
                            flights: list[list[int]],
                            src: int,
                            dst: int,
                            k: int
                            ) -> int:
        print("[Basic BF]")
                
        prev_state = [math.inf for _ in range(n)]
        cur_state = [math.inf for _ in range(n)]
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