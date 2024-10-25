"""
#bfs, #dfs, #dp, #dag, #backtracking

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in 
any order.

The graph is given as follows: graph[i] is a list of all nodes you can 
visit from node i (i.e., there is a directed edge from node i to node 
graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""
import collections
from functools import lru_cache


class Solution:
    def bfs_approach(self, graph: list[list[int]]) -> list[list[int]]:
        print("[BFS]")

        queue = collections.deque()
        all_paths = []

        start_node = 0
        target = len(graph) - 1
        start_path = [[start_node], 0]
        queue.append(start_path)

        while queue:
            cur_path, cur_node = queue.popleft()

            for next_node in graph[cur_node]:
                new_path = cur_path[:]
                new_path.append(next_node)

                if next_node == target:
                    all_paths.append(new_path)
                else:
                    queue.append([new_path, next_node])

        return all_paths

    def dfs_approach(self, graph: list[list[int]]) -> list[list[int]]:
        print("[DFS]")

        all_paths = []
        target = len(graph) - 1

        def dfs(cur_node: int, cur_path: int):
            if cur_node == target:
                all_paths.append(list(cur_path))
                return

            for next_node in graph[cur_node]:
                cur_path.append(next_node)
                dfs(next_node, cur_path)
                cur_path.pop()

        start_node = 0
        start_path = collections.deque()
        start_path.append(start_node)
        dfs(start_node, start_path)

        return all_paths

    def dp_approach(self, graph: list[list[int]]) -> list[list[int]]:
        print("[DP]")

        target = len(graph) - 1

        @lru_cache(maxsize=None)
        def dp(cur_node: int) -> list[list[int]]:
            if cur_node == target:
                return [[target]]

            result_path = []
            for next_node in graph[cur_node]:
                for path in dp(next_node):
                    result_path.append([cur_node] + path)

            return result_path

        start_node = 0
        return dp(start_node)
