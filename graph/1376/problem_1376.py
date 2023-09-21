'''
#dfs, #bfs, #tree, length from root to each node

A company has n employees with a unique ID for each employee from 0 to 
n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where 
manager[i] is the direct manager of the i-th employee, manager[headID] 
= -1. Also, it is guaranteed that the subordination relationships have 
a tree structure.

The head of the company wants to inform all the company employees of an 
urgent piece of news. He will inform his direct subordinates, and they 
will inform their subordinates, and so on until all employees know 
about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his 
direct subordinates (i.e., After informTime[i] minutes, all his direct 
subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about 
the urgent news.

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,
0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager 
of all the employees in the company and needs 1 minute to inform them 
all.
'''
import collections


class Solution:

    def _make_adj_list(self, 
                       n: int, 
                       head_id: int, 
                       manager: list[int]
                       ) -> list[list[int]]:
        
        adj_list = [[] for _ in range(n)]
        for employee in range(n):
            if employee != head_id:
                adj_list[manager[employee]].append(employee)

        return adj_list

    def bfs_approach(self, 
                     n: int, 
                     head_id: int, 
                     manager: list[int], 
                     inform_time: list[int]
                     ) -> int:
        print("[BFS]")
        adj_list = self._make_adj_list(n, head_id, manager)
        queue = collections.deque()                         
        queue.append((head_id, 0))
        max_time = 0

        while queue:
            cur_node, time = queue.popleft()
            
            max_time = max(max_time, time)

            for next_node in adj_list[cur_node]:
                queue.append((next_node, time + inform_time[cur_node]))

        return max_time
    
    def dfs_approach(self, 
                     n: int, 
                     head_id: int, 
                     manager: list[int], 
                     inform_time: list[int]
                     ) -> int:
        print("[DFS]")
        adj_list = self._make_adj_list(n, head_id, manager)
        max_time = 0

        def dfs(cur_node: int, time: int) -> None:
            nonlocal max_time

            max_time = max(max_time, time)

            for next_node in adj_list[cur_node]:
                dfs(next_node, time + inform_time[cur_node])
        dfs(head_id, 0)

        return max_time