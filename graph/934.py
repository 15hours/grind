'''
#bfs, #dfs, #matrix, shortest path between two islands

You are given an n x n binary matrix grid where 1 represents land and 0 
represents water.

An island is a 4-directionally connected group of 1's not connected to 
any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two 
islands.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],
                [1,0,0,0,1],
                [1,0,1,0,1],
                [1,0,0,0,1],
                [1,1,1,1,1]]
Output: 1
'''
import collections


class Solution:
    
    def _bfs_approach(self, 
                      start_node: list[int], 
                      grid: list[list[int]]
                      ) -> int:
                      
        # grid[start_node[0]][start_node[1]] = "+"
        num_rows = len(grid)
        num_cols = len(grid[0])

        shores_queue = collections.deque()
        def dfs(cur_node: list[int]) -> None:
            i, j = cur_node

            if not (0 <= i < num_rows and \
                    0 <= j < num_cols):
                return

            if grid[i][j] == 0:
                grid[i][j] = "+"
                shores_queue.append([[i, j], 1])
            elif grid[i][j] == 1:
                grid[i][j] = "+"

                dfs([i - 1, j])
                dfs([i, j - 1])
                dfs([i + 1, j])
                dfs([i, j + 1])

        dfs(start_node)

        min_steps = 200
        
        while shores_queue:
            cur_node = shores_queue.popleft()
            i,j = cur_node[0]
            steps = cur_node[1]

            if steps >= min_steps:
                continue

            for next_i, next_j in [(i - 1, j), (i, j - 1),
                                   (i + 1, j), (i, j + 1)]:
                if (0 <= next_i < num_rows and \
                        0 <= next_j < num_cols):

                    if grid[next_i][next_j] == 1:
                        min_steps = steps
                    elif grid[next_i][next_j] == 0:
                        grid[next_i][next_j] = "+"
                        shores_queue.append([[next_i, next_j], steps + 1])
                    
        return min_steps   


    def shortest_bridge(self, grid: list[list[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    grid_copy = [[_ for _ in row] for row in grid]
                    return self._bfs_approach([i, j], grid_copy)
        return 


sol = Solution()
print(sol.shortest_bridge([[0,1,0,0,0,0],
                            [0,1,1,1,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [1,1,0,0,0,0]]))
print(sol.shortest_bridge([[1,1,0,0,0],
                            [1,0,0,0,0],
                            [1,0,0,0,0],
                            [0,0,0,1,1],
                            [0,0,0,1,1]]))
print(sol.shortest_bridge([[0,1],[1,0]]))
print(sol.shortest_bridge([[0,1,0],[0,0,0],[0,0,1]]))
print(sol.shortest_bridge([[1,1,1,1,1],
                            [1,0,0,0,1],
                            [1,0,1,0,1],
                            [1,0,0,0,1],
                            [1,1,1,1,1]]))