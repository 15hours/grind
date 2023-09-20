import collections


class Solution:

    def kahn_approach(self, 
                      num_courses: int, 
                      prerequisites: list[list[int]]
                      ) -> bool:
        print("[Kahn's algorithm]")

        adj_list = collections.defaultdict(list)
        indegree = [0 for _ in range(num_courses)]
        for child, parent in prerequisites:
            
            adj_list[parent].append(child)
            indegree[child] += 1

        queue = collections.deque()
        for node in range(num_courses):
            if indegree[node] == 0:
                queue.append(node)

        passed_nodes_count = 0
        while queue:
            cur_node = queue.popleft()
            passed_nodes_count += 1

            for next_node in adj_list[cur_node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)

        return passed_nodes_count == num_courses
    
    def dfs_approach(self,
                     num_courses: int,
                     prerequisites: list[list[int]]
                     ) -> bool:
        print("[DFS]")

        WHITE = 0
        GRAY = 1
        BLACK = 2

        adj_list = collections.defaultdict(list)
        for child, parent in prerequisites:
            if parent == child:
                return False
            
            adj_list[parent].append(child)

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
            return True
        
        for node in range(num_courses):
            if visited[node] == WHITE:
                if not dfs(node):
                    return False
        
        return True