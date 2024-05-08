'''
#bfs, #dfs, #dsu

Given an m x n 2D binary grid grid which represents a map of '1's 
(land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of the 
grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
import collections


class UnionFind:
    def __init__(self, grid: list[list[str]]) -> None:
        num_rows = len(grid)
        num_cols = len(grid[0])

        self.root = list(range(num_rows * num_cols))
        self.rank = [0 for _ in range(num_rows * num_cols)]
        self.count = sum(x.count("1") for x in grid)

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
                self.rank[root_node_2] += self.rank[root_node_1]
                self.count -= 1
            elif self.rank[root_node_2] < self.rank[root_node_1]:
                self.root[root_node_2] = root_node_1
                self.rank[root_node_1] += self.rank[root_node_2]
                self.count -= 1
            else:
                self.root[root_node_2] = root_node_1
                self.rank[root_node_1] += 1
                self.count -= 1

    def return_count(self) -> int:
        return self.count


class Solution:

    def bfs_approach(self, grid: list[list[str]]) -> None:
        print("[BFS]")

        num_rows = len(grid)
        num_cols = len(grid[0])
        grid_copy = [row[:] for row in grid]

        def bfs(start_node: list[int]) -> None:
            grid_copy[start_node[0]][start_node[1]] = "+"

            queue = collections.deque()
            queue.append(start_node)

            while queue:
                cur_node = queue.popleft()
                i, j = cur_node

                for next_i, next_j in [(i - 1, j), (i, j - 1),
                                       (i + 1, j), (i, j + 1)]:
                    if not (0 <= next_i < num_rows and
                            0 <= next_j < num_cols and
                            grid_copy[next_i][next_j] == "1"):
                        continue

                    grid_copy[next_i][next_j] = "+"
                    queue.append([next_i, next_j])

        count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid_copy[i][j] == "1":
                    count += 1
                    bfs([i, j])

        return count

    def dfs_approach(self, grid: list[list[int]]) -> None:
        print("[DFS]")

        num_rows = len(grid)
        num_cols = len(grid[0])
        grid_copy = [row[:] for row in grid]

        def dfs(cur_node: list[int]) -> None:
            i, j = cur_node

            if not (0 <= i < num_rows and
                    0 <= j < num_cols and
                    grid_copy[i][j] == "1"):
                return

            grid_copy[i][j] = "+"

            dfs([i - 1, j])
            dfs([i, j - 1])
            dfs([i + 1, j])
            dfs([i, j + 1])

        count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid_copy[i][j] == "1":
                    count += 1
                    dfs([i, j])

        return count

    def dsu_approach(self, grid: list[list[str]]) -> int:
        print("[DSU]")

        num_rows = len(grid)
        num_cols = len(grid[0])

        uf = UnionFind(grid)

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1":
                    cur_node = i * num_cols + j
                    if j + 1 < num_cols and grid[i][j + 1] == "1":
                        node_right = cur_node + 1
                        uf.union(cur_node, node_right)
                    if i + 1 < num_rows and grid[i + 1][j] == "1":
                        node_below = cur_node + num_cols
                        uf.union(cur_node, node_below)

        return uf.return_count()
