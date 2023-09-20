'''
#dfs, #kahn, #cycling

There are a total of numCourses courses you have to take, labeled from 
0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi 
first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have 
to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. If it is 
impossible to finish all courses, return an empty array.
 
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 
you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 
you should have finished both courses 1 and 2. Both courses 1 and 2 
should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is 
[0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
'''
import collections


class Solution:

    def kahn_approach(self, 
                      num_courses: int, 
                      prerequisites: list[list[int]]
                      ) -> list[int]:
        print("[Kahn's algorithm]")

        adj_list = collections.defaultdict(list)
        indegree = [0 for _ in range(num_courses)]
        for child, parent in prerequisites:
            adj_list[parent].append(child)
            indegree[child] += 1

        answer = []
        queue = collections.deque()
        for node in range(num_courses):
            if indegree[node] == 0:
                queue.append(node)
                answer.append(node)

        while queue:
            cur_node = queue.popleft()

            for next_node in adj_list[cur_node]:
                indegree[next_node] -= 1

                if indegree[next_node] == 0:
                    queue.append(next_node)
                    answer.append(next_node)

        if len(answer) != num_courses:
            return []
        
        return answer

    def dfs_approach(self, 
                     num_courses: int, 
                     prerequisites: list[list[int]]
                     ) -> list[int]:
        print("[DFS]")

        WHITE = 0
        GRAY = 1
        BLACK = 2

        adj_list = collections.defaultdict(list)
        for child, parent in prerequisites:
            adj_list[child].append(parent)

        answer = []
        visited = [WHITE for _ in range(num_courses)]
        def dfs(cur_node: int) -> bool:
            if visited[cur_node] == GRAY:
                return False
            if visited[cur_node] == BLACK:
                return True
            
            visited[cur_node] = GRAY
            for next_node in adj_list[cur_node]:
                if not dfs(next_node):
                    return False
                
            visited[cur_node] = BLACK
            answer.append(cur_node)
            return True

        for node in range(num_courses):
            if visited[node] == WHITE:  
                if not dfs(node):
                    return []
            
        return answer
