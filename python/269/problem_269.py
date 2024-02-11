'''
#dfs, #kahn, #coloring

There is a new alien language that uses the English alphabet. However, 
the order of the letters is unknown to you.

You are given a list of strings words from the alien language's 
dictionary. Now it is claimed that the strings in words are 
sorted lexicographically
 by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in 
words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien 
language sorted in lexicographically increasing order by the new 
language's rules. If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
'''
import collections


class Solution:

    def kahn_approach(self, words: list[str]) -> str:
        print("[Kahn's algorithm]")

        adj_list = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        for word in words:
            for ch in word:
                node = ord(ch) - ord('a')
                indegree[node] = 0

        for word_1, word_2 in zip(words, words[1:]):
            for ch_1, ch_2 in zip(word_1, word_2):
                if ch_1 == ch_2:
                    continue
                
                node_1, node_2 = ord(ch_1) - ord('a'), ord(ch_2) - ord('a')
                if node_2 not in adj_list[node_1]:
                    adj_list[node_1].add(node_2)
                    indegree[node_2] += 1
                break
            else:
                if len(word_1) > len(word_2):
                    return ""

        queue = collections.deque()
        for node, degree in indegree.items():
            if degree == 0:
                queue.append(node)
                

        answer = []   
        while queue:
            cur_node = queue.popleft()
            answer.append(chr(cur_node + ord('a')))

            for next_node in adj_list[cur_node]:
                indegree[next_node] -= 1
                
                if indegree[next_node] == 0:
                    queue.append(next_node)

        if len(answer) != len(adj_list):
            return ""
        return "".join(answer)
    
    def dfs_approach(self, words: list[str]) -> str:
        print("[DFS]")

        WHITE = 0
        GRAY = 1
        BLACK = 2
        
        adj_list = collections.defaultdict(set)
        visited = collections.defaultdict(int)
        for word in words:
            for ch in word:
                node = ord(ch) - ord('a')
                visited[node] = WHITE
        
        for word_1, word_2 in zip(words, words[1:]):
            for ch_1, ch_2 in zip(word_1, word_2):
                if ch_1 == ch_2:
                    continue

                node_1, node_2 = ord(ch_1) - ord('a'), ord(ch_2) - ord('a')
                if node_2 not in adj_list[node_1]:
                    adj_list[node_1].add(node_2)
                    visited[node_1] = 0
                    visited[node_2] = 0
                break
            else:
                if len(word_1) > len(word_2):
                    return ""
                
        answer = []
        def dfs(cur_node: int) -> bool:
            nonlocal answer

            if visited[cur_node] == GRAY:
                return False
            if visited[cur_node] == BLACK:
                return True
            
            visited[cur_node] = GRAY
            for next_node in adj_list[cur_node]:
                if not dfs(next_node):
                    return False
                
            visited[cur_node] = BLACK
            answer = [chr(cur_node + ord('a'))] + answer
            return True

        for node, vis in visited.items():
            if vis == WHITE:
                if not dfs(node):
                    return ""
                
        if len(answer) != len(adj_list):
            return ""
        return "".join(answer)