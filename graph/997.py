'''
#indegree, #outdegree

In a town, there are n people labeled from 1 to n. There is a rumor 
that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing 
that the person labeled ai trusts the person labeled bi. If a trust 
relationship does not exist in trust array, then such a trust 
relationship does not exist.

Return the label of the town judge if the town judge exists and can be 
identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
'''

class Solution:

    def two_array_approach(self, n: int, trust: list[list[int]]):
        indegree = [0 for _ in range(n)]
        outdegree = [0 for _ in range(n)]
        for connection in trust:
            ai, bi = connection

            outdegree[ai - 1] += 1
            indegree[bi - 1] += 1
        
        for i in range(n):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i + 1
        return -1

    def one_array_approach(self, n: int , trust: list[list[int]]):
        inout =  [0 for _ in range(n)]
        
        for connection in trust:
            ai, bi = connection

            inout[bi - 1] += 1
            inout[ai - 1] -= 1

        for i in range(n):
            if inout[i] == n - 1:
                return i + 1
        return -1
    
    def findJudge(self, 
                  n: int, 
                  trust: list[list[int]]
                  ) -> int:
        # return self.two_array_approach(n, trust)
        return self.one_array_approach(n, trust)