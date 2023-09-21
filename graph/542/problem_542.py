'''
#bfs, #dp, #matrix, steps count between "water" tiles and "island" tiles

Given an m x n binary matrix mat, return the distance of the nearest 0 
for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''
import collections
import math


class Solution:

    def _create_queue(self, 
                      mat: list[list[int]], 
                      num_rows: int, 
                      num_cols: int
                      ) -> list[tuple[int, ...]]: 
        
        queue = collections.deque()
        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1

        return queue

    def bfs_approach(self, mat: list[list[int]]) -> list[list[int]]:
        print("[BFS]")
        num_rows = len(mat)
        num_cols = len(mat[0])
        mat_copy = [row[:] for row in mat]

        queue = self._create_queue(mat_copy, num_rows, num_cols)

        while queue:
            i, j = queue.popleft()

            for next_i, next_j in [(i - 1, j), (i, j - 1),
                                   (i + 1, j), (i, j + 1)]:
                if (0 <= next_i < num_rows and \
                        0 <= next_j < num_cols and \
                        mat_copy[next_i][next_j] == -1):
                    mat_copy[next_i][next_j] = mat_copy[i][j] + 1
                    queue.append([next_i, next_j])

        return mat_copy
    
    def dp_approach(self, mat: list[list[int]]) -> list[list[int]]:
        print("[DP]")
        num_rows = len(mat)
        num_cols = len(mat[0])
        mat_copy = [row[:] for row in mat]

        for i in range(num_rows):
            for j in range(num_cols):
                if mat_copy[i][j] == 0:
                    continue
                
                min_neighbor = math.inf
                if i > 0:
                    min_neighbor = min(min_neighbor, mat_copy[i - 1][j])
                if j > 0:
                    min_neighbor = min(min_neighbor, mat_copy[i][j - 1])
                
                mat_copy[i][j] = min_neighbor + 1

        for i in range(num_rows - 1, -1, -1):
            for j in range(num_cols - 1, -1, -1):
                if mat_copy[i][j] == 0:
                    continue
                
                min_neighbor = math.inf
                if i < num_rows - 1:
                    min_neighbor = min(min_neighbor, mat_copy[i + 1][j])
                if j < num_cols - 1:
                    min_neighbor = min(min_neighbor, mat_copy[i][j + 1])
                
                mat_copy[i][j] = min(mat_copy[i][j], min_neighbor + 1)
        
        return mat_copy