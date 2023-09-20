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

    def _bfs_approach(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        queue = self._create_queue(mat, num_rows, num_cols)

        while queue:
            i, j = queue.popleft()

            for next_i, next_j in [(i - 1, j), (i, j - 1),
                                   (i + 1, j), (i, j + 1)]:
                if (0 <= next_i < num_rows and \
                        0 <= next_j < num_cols and \
                        mat[next_i][next_j] == -1):
                    mat[next_i][next_j] = mat[i][j] + 1
                    queue.append([next_i, next_j])

        return mat
    
    def _dp_solution(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 0:
                    continue
                
                min_neighbor = math.inf
                if i > 0:
                    min_neighbor = min(min_neighbor, mat[i - 1][j])
                if j > 0:
                    min_neighbor = min(min_neighbor, mat[i][j - 1])
                
                mat[i][j] = min_neighbor + 1

        for i in range(num_rows - 1, -1, -1):
            for j in range(num_cols - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                
                min_neighbor = math.inf
                if i < num_rows - 1:
                    min_neighbor = min(min_neighbor, mat[i + 1][j])
                if j < num_cols - 1:
                    min_neighbor = min(min_neighbor, mat[i][j + 1])
                
                mat[i][j] = min(mat[i][j], min_neighbor + 1)
        
        return mat
                    
                
    def update_matrix(self, mat: list[list[int]]) -> list[list[int]]:
        mat_copy = [row[:] for row in mat]
        # return self._bfs_approach(mat_copy)    
        return self._dp_solution(mat_copy)


sol = Solution()
mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
print(sol.update_matrix(mat))
