'''
#bfs

You are given an m x n matrix maze (0-indexed) with empty cells 
(represented as '.') and walls (represented as '+'). You are also given 
the entrance of the maze, where entrance = [entrancerow, entrancecol] 
denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot 
step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. An exit is 
defined as an empty cell that is at the border of the maze. The 
entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to 
the nearest exit, or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], 
entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], 
entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
'''
import collections


class Solution:

    def _restore_data(self,
                      maze: list[list[str]],
                      entrance: list[int]
                      ) -> int:

        num_rows = len(maze)
        num_cols = len(maze[0])

        def dfs(cur_node: list[int]) -> None:
            i, j = cur_node

            for next_i, next_j in [(i - 1, j), (i, j - 1),
                                   (i + 1, j), (i, j + 1)]:
                if (0 <= next_i < num_rows and
                        0 <= next_j < num_cols and
                        maze[next_i][next_j] == "-"):
                    maze[next_i][next_j] = "."
                    dfs([next_i, next_j])
        dfs(entrance)

    def bfs_approach(self,
                     maze: list[list[str]],
                     entrance: list[int]
                     ) -> int:
        print("[BFS]")

        maze_copy = [row[:] for row in maze]
        num_rows = len(maze_copy)
        num_cols = len(maze_copy[0])

        queue = collections.deque()
        steps = 0

        maze_copy[entrance[0]][entrance[1]] = "-"
        queue.append([entrance, steps])

        while queue:
            cur_node = queue.popleft()
            i, j = cur_node[0]
            steps = cur_node[1]

            is_exit = ((i == 0 or i == num_rows - 1 or
                        j == 0 or j == num_cols - 1) and
                       cur_node[0] != entrance)
            if is_exit:
                return steps

            for next_i, next_j in [(i - 1, j), (i, j - 1),
                                   (i + 1, j), (i, j + 1)]:
                if (0 <= next_i < num_rows and
                        0 <= next_j < num_cols and
                        maze_copy[next_i][next_j] == "."):
                    maze_copy[next_i][next_j] = "-"
                    queue.append([[next_i, next_j], steps + 1])

        return -1
