'''
#bfs, #dfs, #dsu

You are given an m x n binary matrix grid, where 0 represents a sea 
cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent 
(4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off 
the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that 
is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the 
boundary.
'''
import collections


class UnionFind:
    def __init__(self, grid: list[list[int]]) -> None:
        num_rows = len(grid)
        num_cols = len(grid[0])

        self.root = list(range(num_rows * num_cols))
        self.rank = [1 for _ in range(num_rows * num_cols)]
        self.border = [False for _ in range(num_rows * num_cols)]

        for i in [0, num_rows - 1]:
            for j in range(num_cols):
                if grid[i][j] == 1:
                    self.border[i * num_cols + j] = True
        for j in [0, num_cols - 1]:
            for i in range(num_rows):
                if grid[i][j] == 1:
                    self.border[i * num_cols + j] = True

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node_1: int, node_2: int) -> None:
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 != root_node_2:
            if self.rank[root_node_1] < self.rank[root_node_2]:
                self.root[root_node_1] = root_node_2
                self.border[root_node_2] |= self.border[root_node_1]
                self.rank[root_node_2] += self.rank[root_node_1]

            else:
                self.root[root_node_2] = root_node_1
                self.border[root_node_1] |= self.border[root_node_2]
                self.rank[root_node_1] += self.rank[root_node_2]

    def connected_to_border(self, node: int) -> int:
        return self.border[self.find(node)]


class Solution:

    def bfs_approach(self, grid: list[list[int]]) -> int:
        print("[BFS]")

        grid_copy = [row[:] for row in grid]
        num_rows = len(grid_copy)
        num_cols = len(grid_copy[0])
        num_ones = sum(x.count(1) for x in grid_copy)

        queue = collections.deque()
        connected_1s_counter = 0

        for i in [0, num_rows - 1]:
            for j in range(num_cols):
                if grid_copy[i][j] == 1:
                    connected_1s_counter += 1
                    grid_copy[i][j] = "+"
                    queue.append([i, j])

        for j in [0, num_cols - 1]:
            for i in range(num_rows):
                if grid_copy[i][j] == 1:
                    connected_1s_counter += 1
                    grid_copy[i][j] = "+"
                    queue.append([i, j])

        while queue:
            cur_node = queue.popleft()
            i, j = cur_node

            for next_i, next_j in [(i - 1, j), (i, j - 1),
                                   (i + 1, j), (i, j + 1)]:
                if (0 <= next_i < num_rows and
                        0 <= next_j < num_cols and
                        grid_copy[next_i][next_j] == 1):
                    connected_1s_counter += 1
                    grid_copy[next_i][next_j] = "+"
                    queue.append([next_i, next_j])

        return num_ones - connected_1s_counter

    def dfs_approach(self, grid: list[list[int]]) -> int:
        print("[DFS]")

        grid_copy = [row[:] for row in grid]
        num_rows = len(grid_copy)
        num_cols = len(grid_copy[0])
        num_ones = sum(x.count(1) for x in grid_copy)
        connected_1s_counter = 0

        def dfs(cur_node: list[int]) -> int:
            nonlocal connected_1s_counter
            i, j = cur_node

            if not (0 <= i < num_rows and
                    0 <= j < num_cols and
                    grid_copy[i][j] == 1):
                return

            connected_1s_counter += 1
            grid_copy[i][j] = "+"

            dfs([i - 1, j])
            dfs([i, j - 1])
            dfs([i + 1, j])
            dfs([i, j + 1])

        for i in [0, num_rows - 1]:
            for j in range(num_cols):
                if grid_copy[i][j] == 1:
                    dfs([i, j])

        for j in [0, num_cols - 1]:
            for i in range(num_rows):
                if grid_copy[i][j] == 1:
                    dfs([i, j])

        return num_ones - connected_1s_counter

    def dsu_approach(self, grid: list[list[int]]) -> int:
        print("[DSU]")

        grid_copy = [row[:] for row in grid]
        num_rows = len(grid_copy)
        num_cols = len(grid_copy[0])
        uf = UnionFind(grid_copy)

        for i in range(num_rows):
            for j in range(num_cols):
                if grid_copy[i][j] == 0:
                    continue

                cur_node = i * num_cols + j
                if i + 1 < num_rows and grid_copy[i + 1][j] == 1:
                    bottom_node = cur_node + num_cols
                    uf.union(cur_node, bottom_node)
                if j + 1 < num_cols and grid_copy[i][j + 1] == 1:
                    right_node = cur_node + 1
                    uf.union(cur_node, right_node)

        isolated_1s_counter = 0

        for i in range(1, num_rows - 1):
            for j in range(1, num_cols - 1):
                if (grid_copy[i][j] == 1 and
                        not uf.connected_to_border(i * num_cols + j)):
                    isolated_1s_counter += 1

        return isolated_1s_counter
