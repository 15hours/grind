'''
#bfs

A gene string can be represented by an 8-character long string, with 
choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene 
to a gene string endGene where one mutation is defined as one single 
character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation. There is also a 
gene bank bank that records all the valid gene mutations. A gene must 
be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank 
bank, return the minimum number of mutations needed to mutate from 
startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be 
included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", 
        bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
'''
import collections


class Solution:

    def bfs_approach(self,
                     start_gene: int,
                     end_gene: int,
                     bank: list[str]
                     ) -> int:
        print("[BFS]")

        start_node = start_gene
        target = end_gene

        queue = collections.deque()
        queue.append([start_node, 0])

        bank_set = set(bank)

        while queue:
            cur_node, steps = queue.popleft()
            if cur_node == target:
                return steps

            for i in range(len(cur_node)):
                for c in 'ACGT':
                    next_possible_node = cur_node[:i] + c + cur_node[i+1:]

                    if next_possible_node in bank_set:
                        bank_set.remove(next_possible_node)
                        queue.append([next_possible_node, steps + 1])

        return -1
