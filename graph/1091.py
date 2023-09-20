'''
#bfs, #matrix traversal

Given an n x n binary matrix grid, return the length of the shortest 
clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., 
(0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., 
they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
'''
import collections


class Solution:

    def _bfs_approach(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        if grid[0][0] == 1 or grid[num_rows - 1][num_cols - 1] == 1:
            return -1
        
        queue = collections.deque()
        queue.append([[0, 0], 1])
        grid[0][0] = 1
        
        directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), 
                      (1, 0), (1, 1), (0, 1), (-1, 1)]
        while queue:
            cur_node, steps = queue.popleft()
            i, j = cur_node
            if i == num_rows - 1 and j == num_cols - 1:
                return steps

            for shift_i, shift_j in directions:
                next_i, next_j = i + shift_i, j + shift_j

                if (0 <= next_i < num_rows and \
                        0 <= next_j < num_cols and \
                        grid[next_i][next_j] == 0):
                    grid[next_i][next_j] = 1
                    queue.append([[next_i, next_j], steps + 1])

        return -1

    def shortest_path_binary_matrix(self, grid: list[list[int]]) -> int:
        grid_copy = [row[:] for row in grid]
        return self._bfs_approach(grid_copy)
        

sol = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(sol.shortest_path_binary_matrix(grid))