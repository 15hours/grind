'''
#bfs, #dfs

There are n cities numbered from 0 to n - 1 and n - 1 roads such that 
there is only one way to travel between two different cities (this 
network form a tree). Last year, The ministry of transport decided to 
orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] 
represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many 
people want to travel to this city.

Your task consists of reorienting some roads such that each city can 
visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each 
node can reach the node 0 (capital).

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each 
node can reach the node 0 (capital).
'''
import collections


class Solution:

    def _make_adj_list(self,
                       n: int,
                       connections: list[list[int]]
                       ) -> [list[list[int]], list[list[int]]]:

        adj_list = [[] for _ in range(n)]
        bidir_adj_list = [[] for _ in range(n)]

        for connection in connections:
            adj_list[connection[0]].append(connection[1])
            bidir_adj_list[connection[0]].append(connection[1])
            bidir_adj_list[connection[1]].append(connection[0])

        return adj_list, bidir_adj_list

    def bfs_approach(self,
                     n: int,
                     connections: list[list[int]]
                     ) -> int:
        print("[BFS]")

        adj_list, bidir_adj_list = self._make_adj_list(n, connections)
        queue = collections.deque()
        visited = [False for _ in range(n)]

        start_node = 0
        visited[start_node] = True
        queue.append(start_node)

        wrong_paths_count = 0

        while queue:
            cur_node = queue.popleft()

            for next_node in bidir_adj_list[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True

                    if next_node in adj_list[cur_node]:
                        wrong_paths_count += 1

                    queue.append(next_node)

        return wrong_paths_count

    def dfs_approach(self,
                     n: int,
                     connections: list[list[int]]
                     ) -> int:
        print("[DFS]")

        adj_list, bidir_adj_list = self._make_adj_list(n, connections)
        start_node = 0
        wrong_paths_count = 0

        def dfs(cur_node: int, parent: int) -> None:
            nonlocal wrong_paths_count

            for next_node in bidir_adj_list[cur_node]:
                if next_node != parent:
                    if next_node in adj_list[cur_node]:
                        wrong_paths_count += 1

                    dfs(next_node, cur_node)
        dfs(start_node, -1)

        return wrong_paths_count
