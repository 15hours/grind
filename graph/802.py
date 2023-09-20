'''
#dfs, #kahn, #kahn algorithm, #orgraph, #loops

There is a directed graph of n nodes with each node labeled from 0 
to n - 1. The graph is represented by a 0-indexed 2D integer array graph
where graph[i] is an integer array of nodes adjacent to node i, meaning
there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is 
a safe node if every(!) possible path starting from that node leads to 
a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer 
should be sorted in ascending order.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from 
either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 
or 6.
'''

import collections


class Solution:
    
    def _dfs_approach(self, graph: list[list[int]]) -> list[int]:
        num_nodes = len(graph)
        # -1 - not explored
        #  0 - start exploring
        #  1 - visited
        visited = [-1 for _ in range(num_nodes)] 
        safe_nodes = []

        def dfs(cur_node: int) -> bool:
            visited[cur_node] = 0

            for next_node in graph[cur_node]:
                if (visited[next_node] == 0 or \
                        visited[next_node] == -1 and not dfs(next_node)):
                    return False

            visited[cur_node] = 1
            safe_nodes.append(cur_node)
            return True 
        
        for next_node in range(num_nodes):
            if visited[next_node] == -1:
                dfs(next_node)

        return sorted(safe_nodes)

    def _kahn_solution(self, graph: list[list[int]]) -> list[int]:
        num_nodes = len(graph)

        reversed_graph = collections.defaultdict(list)
        queue = collections.deque()
        outdegree = collections.defaultdict(int)
        safe_nodes = []

        for node in range(num_nodes):
            for neighbor in graph[node]:
                reversed_graph[neighbor].append(node)
            if graph[node]:
                outdegree[node] = len(graph[node])
            else:
                queue.append(node)
                safe_nodes.append(node)
        
        while queue:
            cur_node = queue.popleft()

            for incoming_node in reversed_graph[cur_node]:
                outdegree[incoming_node] = outdegree[incoming_node] - 1
                if outdegree[incoming_node] == 0:
                    queue.append(incoming_node)
                    safe_nodes.append(incoming_node)

        return sorted(safe_nodes)

            


    def eventual_safe_nodes(self, graph: list[list[int]]) -> list[int]:
        return self._dfs_approach(graph)
        # return self._kahn_solution(graph)
        

sol = Solution()
mat = [[1,2],[2,3],[5],[0],[5],[],[]]
print(sol.eventual_safe_nodes(mat))
mat = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(sol.eventual_safe_nodes(mat))
mat = [[0,6,7,9],[],[],[],[2,6,8],[7,9],[7,8,9],[],[6,9],[7]]
print(sol.eventual_safe_nodes(mat))
