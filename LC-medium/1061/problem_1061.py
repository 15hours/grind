'''
#dfs, #dsu, #coloring

You are given two strings of the same length s1 and s2 and a string 
baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 
'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence 
relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and 
s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", 
and "aab" is the lexicographically smallest equivalent string of 
baseStr.

Return the lexicographically smallest equivalent string of baseStr by 
using the equivalency information from s1 and s2.

Example 1:
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can 
group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in 
lexicographical order.
So the answer is "makkek".

Example 2:
Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can 
group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer 
is "hdld".

Example 3:
Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as 
[a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr 
except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
'''
import collections


class UnionFind:
    def __init__(self, num_nodes: int) -> None:
        self.root = list(range(num_nodes))
        self.rank = [1 for _ in range(num_nodes)]

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node_1: int, node_2: int) -> None:
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 == root_node_2:
            return

        if root_node_1 < root_node_2:
            self.root[root_node_2] = root_node_1
            self.rank[root_node_1] += self.rank[root_node_2]
        else:
            self.root[root_node_1] = root_node_2
            self.rank[root_node_2] += self.rank[root_node_1]


class Solution:

    def dsu_approach(self,
                     s_1: str,
                     s_2: str,
                     base_str: str
                     ) -> str:
        print("[DSU]")

        uf = UnionFind(26)

        for ch_1, ch_2 in zip(s_1, s_2):
            if ch_1 == ch_2:
                continue
            node_1, node_2 = ord(ch_1) - ord('a'), ord(ch_2) - ord('a')
            uf.union(node_1, node_2)

        answer = str()
        for ch in base_str:
            ascii_code = uf.find(ord(ch) - ord('a')) + ord('a')
            answer += chr(ascii_code)

        return answer

    def dfs_approach(self,
                     s_1: str,
                     s_2: str,
                     base_str: str
                     ) -> str:
        print("[DFS]")

        adj_list = collections.defaultdict(list)
        for ch_1, ch_2 in zip(s_1, s_2):
            if ch_1 == ch_2:
                continue

            node_1, node_2 = ord(ch_1) - ord('a'), ord(ch_2) - ord('a')
            if node_2 not in adj_list[node_1]:
                adj_list[node_1].append(node_2)
            if node_1 not in adj_list[node_2]:
                adj_list[node_2].append(node_1)

        color = [-1 for _ in range(26)]

        def dfs(cur_node: int, graph_color: int) -> None:
            if color[cur_node] == -1:
                color[cur_node] = graph_color
                for next_node in adj_list[cur_node]:
                    dfs(next_node, graph_color)

        for node in range(26):
            if color[node] == -1:
                root_color = node
                dfs(node, root_color)

        answer = str()
        for ch in base_str:
            node_color = color[ord(ch) - ord('a')]
            answer += chr(node_color + ord('a'))

        return answer
