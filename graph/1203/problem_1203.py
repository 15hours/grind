'''
#kahn, #ootb

There are n items each belonging to zero or one of m groups where
group[i] is the group that the i-th item belongs to and it's equal to -1
if the i-th item belongs to no group. The items and the groups are zero
indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the
sorted list. There are some relations between these items where
beforeItems[i] is a list containing all the items that should come
before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an
empty list if there is no solution.


Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
[[],[6],[5],[6],[3,6],[],[],[]]

Output: [6,3,4,1,5,2,0,7]


Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
[[],[6],[5],[6],[3],[],[4],[]]

Output: []

Explanation: This is the same as example 1 except that 4 needs to be
before 6 in the sorted list.
'''
import collections


class Solution:

    def kahn_approach(self,
                      num_nodes: int,
                      num_groups: int,
                      group: list[int],
                      before_items: list[list[int]]
                      ) -> list[int]:
        print("[Kahn's algorithm]")

        unique_group_id = num_groups
        for node in range(num_nodes):
            if group[node] == -1:
                group[node] = unique_group_id
                unique_group_id += 1

        adj_list_nodes = collections.defaultdict(list)
        adj_list_groups = collections.defaultdict(list)
        indegree_nodes = [0 for _ in range(num_nodes)]
        indegree_group = [0 for _ in range(unique_group_id)]
        for node in range(num_nodes):
            for parent in before_items[node]:
                adj_list_nodes[parent].append(node)
                indegree_nodes[node] += 1
                if group[parent] != group[node]:
                    if group[node] not in adj_list_groups[group[parent]]:
                        adj_list_groups[group[parent]].append(group[node])
                        indegree_group[group[node]] += 1
        
        def topological_sort(adj_list: dict[int, list[int]], 
                             indegree: list[int]
                             ) -> list[int]:

            sorted_items = []
            queue = collections.deque()
            for node in range(len(indegree)):
                if indegree[node] == 0:
                    queue.append(node)

            while queue:
                cur_node = queue.popleft()
                sorted_items.append(cur_node)
                
                for next_node in adj_list[cur_node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        queue.append(next_node)
            
            if len(indegree) != len(sorted_items):
                return []
            return sorted_items
                        
        sorted_nodes = topological_sort(adj_list_nodes, indegree_nodes)
        sorted_groups = topological_sort(adj_list_groups, indegree_group)
        if not sorted_nodes or not sorted_groups:
            return []
            
        sorted_nodes_in_groups = collections.defaultdict(list)
        for node in sorted_nodes:
            sorted_nodes_in_groups[group[node]].append(node)
        answer = []
        for cur_group in sorted_groups:
            answer += sorted_nodes_in_groups[cur_group]

        return answer