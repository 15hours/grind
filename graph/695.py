'''
#bfs, #dfs, #dsu

You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the 
island.

Return the maximum area of an island in grid. If there is no island, 
return 0.


Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 
4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''
import collections


class UnionFind:
    def __init__(self, grid: list[list[int]]) -> None:
        num_rows = len(grid)
        num_cols = len(grid[0])

        self.root = list(range(num_rows * num_cols))
        self.size = [0 for _ in range(num_rows * num_cols)]

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    self.size[i * num_cols + j] = 1

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node_1: int, node_2: int) -> None:
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 != root_node_2:
            if self.size[root_node_1] < self.size[root_node_2]:
                self.root[root_node_1] = root_node_2
                self.size[root_node_2] += self.size[root_node_1]
            elif self.size[root_node_2] < self.size[root_node_1]:
                self.root[root_node_2] = root_node_1
                self.size[root_node_1] += self.size[root_node_2]
            else:
                self.root[root_node_2] = root_node_1
                self.size[root_node_1] += self.size[root_node_2]
    
    def num_islands(self, node: int) -> int:
        return self.size[self.find(node)]
    


class Solution:

    def _bfs_approach(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(start_node: int) -> int:
            queue = collections.deque()
            land_count = 1
            
            queue.append(start_node)
        
            while queue:
                i, j = queue.popleft()

                for next_i, next_j in [(i - 1, j), (i, j - 1),
                                       (i + 1, j), (i, j + 1)]:
                    if not (0 <= next_i < num_rows and \
                            0 <= next_j < num_cols and \
                            grid[next_i][next_j] == 1):
                        continue
                    
                    grid[next_i][next_j] = "+"
                    queue.append([next_i, next_j])
                    land_count += 1

            return land_count
        
        max_area = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    grid[i][j] = "+"
                    area = bfs([i, j])
                    max_area = max(max_area, area)

        return max_area
            
    def _dfs_approach(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(cur_cell: list[int]) -> int:
            i, j = cur_cell
            if not (0 <= i < num_rows and \
                    0 <= j < num_cols and \
                    grid[i][j] == 1):
                return 0
            
            grid[i][j] = "+"

            upper_cell = dfs([i - 1, j])
            left_cell = dfs([i, j - 1])
            bottom_cell = dfs([i + 1, j])
            right_cell = dfs([i, j + 1])

            return 1 + upper_cell + left_cell + bottom_cell + right_cell

        max_area = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    area = dfs([i , j])
                    max_area = max(max_area, area)
        
        return max_area

    def _dsu_approach(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        uf = UnionFind(grid)

        max_area = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    continue

                cur_node = i * num_cols + j
                if i + 1 < num_rows and grid[i + 1][j] == 1:
                    bottom_node = cur_node + num_cols
                    uf.union(cur_node, bottom_node)

                if j + 1 < num_cols and grid[i][j + 1] == 1:
                    right_node = cur_node + 1
                    uf.union(cur_node, right_node)

                max_area = max(max_area, uf.num_islands(cur_node))

        return max_area

    def max_area_of_island(self, grid: list[list[int]]) -> int:
        grid_copy = [row[:] for row in grid]
        # return self._bfs_approach(grid_copy)
        # return self._dfs_approach(grid_copy)
        return self._dsu_approach(grid_copy)
    

sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.max_area_of_island(grid))


        