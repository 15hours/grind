'''
#bfs, #dfs, #dsu

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a 
maximal 4-directionally connected group of 0s and a closed island is an 
island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],
                [1,0,0,0,0,1,1,0],
                [1,0,1,0,1,1,1,0],
                [1,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by 
water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
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
                if grid[i][j] == 0:
                    self.border[i * num_cols + j] = True
        for j in [0, num_cols - 1]:
            for i in range(num_rows):
                if grid[i][j] == 0:
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

    def is_border(self, node: int) -> bool:
        return self.border[self.find(node)]


class Solution:

    def _bfs_approach(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        closed_island_counter = 0

        def bfs(start_node: list[int]) -> bool:
            queue = collections.deque()
            queue.append(start_node)
            is_island = True

            while queue:
                i, j = queue.popleft()

                for next_i, next_j in [(i - 1, j), (i, j - 1),
                                       (i + 1, j), (i, j + 1)]:
                    border = (next_i == 0 or next_j == 0 or \
                              next_i == num_rows - 1 or next_j == num_cols - 1)

                    if not (0 <= next_i < num_rows and\
                            0 <= next_j < num_cols and\
                            grid[next_i][next_j] == 0): 
                        continue
                            
                    grid[next_i][next_j] = 1
                    queue.append([next_i, next_j])
                    
                    if border:
                        is_island = False

            return is_island

        for i in range(1, num_rows - 1):
            for j in range(1, num_cols - 1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    if bfs([i, j]):
                        closed_island_counter += 1

        return closed_island_counter

    def _dfs_approach(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        def dfs(cur_cell: list[int]) -> bool:
            i, j = cur_cell

            if not (0 <= i < num_rows and \
                    0 <= j < num_cols):
                return False
            
            if grid[i][j] == 1:
                return True

            grid[i][j] = 1

            up_cell = dfs([i - 1, j])
            left_cell = dfs([i, j - 1])
            bottom_cell = dfs([i + 1, j])
            right_cell = dfs([i, j + 1])

            return up_cell and left_cell and bottom_cell and right_cell

        closed_island_counter = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0 and dfs([i, j]):
                    closed_island_counter += 1

        return closed_island_counter
    
    def _dsu_approach(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        uf = UnionFind(grid)

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    continue

                cur_node = i * num_cols + j 
                if i + 1 < num_rows and grid[i + 1][j] == 0:
                    bottom_node = cur_node + num_cols
                    uf.union(cur_node, bottom_node)
                if j + 1 < num_cols and grid[i][j + 1] == 0:
                    right_node = cur_node + 1
                    uf.union(cur_node, right_node)

        closed_island_counter = 0
        visited = []
        for i in range(1, num_rows - 1):
            for j in range(1, num_cols - 1):
                if grid[i][j] == 0 and not uf.is_border(i * num_cols + j):
                    root = uf.find(i * num_cols + j)
                    if root not in visited:
                        visited.append(root)
                        closed_island_counter += 1

        return closed_island_counter                    

    def closed_islands(self, grid: list[list[int]]) -> int:
        grid_copy = [row[:] for row in grid]
        # return self._bfs_approach(grid_copy)
        # return self._dfs_approach(grid_copy)
        return self._dsu_approach(grid_copy)
    

sol = Solution()
grid = [[0, 1, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 1]]
print(sol.closed_islands(grid))


grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
print(sol.closed_islands(grid))
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
print(sol.closed_islands(grid))
grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]
print(sol.closed_islands(grid))
grid = [[0,0,1,1,0,1,0,0,1,0],
        [1,1,0,1,1,0,1,1,1,0],
        [1,0,1,1,1,0,0,1,1,0],
        [0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],
        [0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,1,0,0,0,1],
        [1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,1,0]]
print(sol.closed_islands(grid))
