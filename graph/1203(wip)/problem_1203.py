import collections


class Solution:

    def kahn_approach(self,
                      n: int,
                      m: int,
                      group: list[int],
                      before_items: list[list[int]]):
        print("[Kahn's algorithm]")
        adj_list = collections.defaultdict(list)
        indegree = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        groupped = collections.defaultdict(list)

        for node in range(n):
            for parent in before_items[node]:
                adj_list[parent].append(node)
                indegree[node] += 1
                visited[node] = True
                visited[parent] = True
        
        for node in range(n):
            if not visited[node]:
                if group[node] == -1:
                    groupped[m].append(node)