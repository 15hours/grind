'''
#bfs, #dfs

There is an m x n rectangular island that borders both the Pacific 
Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left 
and top edges, and the Atlantic Ocean touches the island's right and 
bottom edges.

The island is partitioned into a grid of square cells. You are given an 
m x n integer matrix heights where heights[r][c] represents the height 
above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to 
neighboring cells directly north, south, east, and west if the 
neighboring cell's height is less than or equal to the current cell's 
height. Water can flow from any cell adjacent to an ocean into the 
ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to both the Pacific 
and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],
                    [3,2,3,4,4],
                    [2,4,5,3,1],
                    [6,7,1,4,5],
                    [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic 
oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the 
Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and 
Atlantic oceans.
'''
import collections


class Solution:

    def bfs_approach(self, heights: list) -> list[list[int]]:
        print("[BFS]")
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()

        for i in range(num_rows):
            pacific_queue.append([i, 0])
            atlantic_queue.append([i, num_cols - 1])
        for j in range(num_cols):
            if j != 0:
                pacific_queue.append([0, j])
            if j != num_cols - 1:
                atlantic_queue.append([num_rows - 1, j])

        def bfs(queue: list[list[int]]) -> list[list[int]]:
            answer = set()

            while queue:
                i, j = queue.popleft()
                answer.add((i, j))

                for next_i, next_j in [(i - 1, j), (i, j - 1),
                                       (i + 1, j), (i, j + 1)]:
                    if not (0 <= next_i < num_rows and \
                            0 <= next_j < num_cols and \
                            (next_i, next_j) not in answer and \
                            heights[i][j] <= heights[next_i][next_j]):
                        continue

                    queue.append([next_i, next_j])

            return answer

        pacific = bfs(pacific_queue)
        atlantic = bfs(atlantic_queue)

        output = list(pacific.intersection(atlantic))
        return [list(node) for node in output]

    def dfs_approach(self, heights: list[list[int]]) -> list[list[int]]:
        print("[DFS]")
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(cur_node: int, answer: int) -> None:  
            answer.add(cur_node)
            
            i, j = cur_node
            for next_i, next_j in [(i - 1, j), (i, j - 1),
                                   (i + 1, j), (i, j + 1)]:
                if not (0 <= next_i < num_rows and \
                        0 <= next_j < num_cols and \
                        (next_i, next_j) not in answer and \
                        heights[i][j] <= heights[next_i][next_j]):
                    continue

                dfs((next_i, next_j), answer)
            
        for i in range(num_rows):
            if (i, 0) not in pacific:
                dfs((i, 0), pacific)
            if (i, num_cols - 1) not in atlantic:
                dfs((i, num_cols - 1), atlantic)
        for j in range(num_cols):
            if (0, j) not in pacific:
                dfs((0, j), pacific)
            if (num_rows - 1, j) not in atlantic:
                dfs((num_rows - 1, j), atlantic)
        
        output = list(pacific.intersection(atlantic))
        return [list(node) for node in output]