'''
#dfs, #dsu, #groups

Two strings, X and Y, are considered similar if either they are 
identical or we can make them equivalent by swapping at most two 
letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 
2), and "rats" and "arts" are similar, but "star" is not similar to 
"tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", 
"rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the 
same group even though they are not similar.  Formally, each group is 
such that a word is in the group if and only if it is similar to at 
least one other word in the group.

We are given a list strs of strings where every string in strs is an 
anagram of every other string in strs. How many groups are there?

Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:
Input: strs = ["omv","ovm"]
Output: 1
'''
import collections


class UnionFind:
    def __init__(self, num_nodes):
        self.root = list(range(num_nodes))
        self.rank = [1 for _ in range(num_nodes)]

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node_1, node_2):
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 != root_node_2:
            if self.rank[root_node_2] <= self.rank[root_node_1]:
                self.root[root_node_2] = root_node_1
                self.rank[root_node_1] += self.rank[root_node_2]
            else:
                self.root[root_node_1] = root_node_2
                self.rank[root_node_2] += self.rank[root_node_1]

class Solution:

    def _identical(self, str_1: str, str_2: str) -> bool:
        if str_1 == str_2:
            return True
        
        diffs_count = 0
        for ch_1, ch_2 in zip(str_1, str_2):
            if diffs_count > 2:
                break
            
            if ch_1 != ch_2:
                diffs_count += 1

        return diffs_count == 2
    
    def dsu_approach(self, strs: list[str]) -> int:
        num_nodes = len(strs)
        uf = UnionFind(num_nodes)
        count = num_nodes
        
        for node_1 in range(num_nodes - 1):
            for node_2 in range(node_1 + 1, num_nodes):
                str_1, str_2 = strs[node_1], strs[node_2]
                if self._identical(str_1, str_2) and \
                        uf.find(node_1) != uf.find(node_2):
                    count -= 1
                    uf.union(node_1, node_2)

        return count
                    
    def dfs_approach(self, strs: list[str]) -> int:
        num_nodes = len(strs)
        adj_list = collections.defaultdict(list)
        for node_1 in range(num_nodes - 1):
            for node_2 in range(node_1 + 1, num_nodes):
                str_1, str_2 = strs[node_1], strs[node_2]
                if self._identical(str_1, str_2):
                    adj_list[node_1].append(node_2)
                    adj_list[node_2].append(node_1)
        
        def dfs(cur_node: int) -> None:
            if visited[cur_node]:
                return
            
            visited[cur_node] = True
            for next_node in adj_list[cur_node]:
                dfs(next_node)

        visited = [False for _ in range(num_nodes)]
        groups_count = 0
        for node in range(num_nodes):
            if not visited[node]:
                groups_count += 1
                dfs(node)

        return groups_count