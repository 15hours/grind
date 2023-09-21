'''
#bfs, #orgraph

You are given an integer n, the number of nodes in a directed graph 
where the nodes are labeled from 0 to n - 1. Each edge is red or blue 
in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from 
node ai to node bi in the graph, and blueEdges[j] = [uj, vj] indicates 
that there is a directed blue edge from node uj to node vj in the graph.

Return an array answer of length n, where each answer[x] is the length 
of the shortest path from node 0 to node x such that the edge colors 
alternate along the path, or -1 if such a path does not exist.

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

Input: n = 5, redEdges = [[0,1],[1,2],[2,3],[3,4]] blueEdges = [[1,2],
[2,3],[3,1]]
Output: [0,1,2,3,7]
'''
import collections


class Solution:

    def bfs_approach(self, 
                     n: int, 
                     red_edges: list[list[int]], 
                     blue_edges: list[list[int]]
                     ) -> list[int]:
        print("[BFS]")
        adj_list = [[] for _ in range(n)]
        for [node, neighbor] in red_edges:
            adj_list[node].append([neighbor, 0])
        for [node, neighbor] in blue_edges:
            adj_list[node].append([neighbor, 1])
        
        answer = [-1 for _ in range(n)]
        answer[0] = 0

        visited = [[False, False] for _ in range(len(answer))] 
        visited[0] = [True, True]

        queue = collections.deque()
        queue.append([0, 0, None])

        while queue:
            cur_node, steps, prev_edge_color = queue.popleft()

            for next_node, edge_color in adj_list[cur_node]:
                if (not visited[next_node][edge_color] and \
                        prev_edge_color != edge_color):
                    visited[next_node][edge_color] = True
                    queue.append([next_node, steps + 1, edge_color])
                    if answer[next_node] == -1:
                        answer[next_node] = steps + 1

        return answer     