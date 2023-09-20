'''
#bfs, #dfs, array traverse

Given an array of non-negative integers arr, you are initially 
positioned at start index of the array. When you are at index i, you 
can jump to i + arr[i] or i - arr[i], check if you can reach any index 
with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
'''
import collections


class Solution:

    def _bfs_approach(self, 
                      arr: list[int], 
                      start: int
                      ) -> bool:

        arr_len = len(arr)
        visited = [False for _ in range(arr_len)]
        queue = collections.deque()
        
        visited[start] = True
        queue.append(start)
        target = 0

        while queue:
            i = queue.popleft()
            if arr[i] == target:
                return True

            for i in [i - arr[i], i + arr[i]]:
                if 0 <= i < arr_len and not visited[i]:
                    visited[i] = True
                    queue.append(i)
            
        return False
    
    def _dfs_approach(self, 
                      arr: list[int], 
                      start: int
                      ) -> bool:

        arr_len = len(arr)
        visited = [False for _ in range(arr_len)]
        target = 0

        def dfs(i: int) -> bool:
            if 0 <= i < arr_len and not visited[i]:
                if arr[i] == target:
                    return True

                visited[i] = True
                return dfs(i - arr[i]) or dfs(i + arr[i])

        return dfs(start)

    def can_reach(self, 
                  arr: list[int], 
                  start: int
                  ) -> bool:
        # return self._bfs_approach(arr, start)
        return self._dfs_approach(arr, start)


# arr = [4,2,3,0,3,1,2]
# start = 5
# arr = [4,2,3,0,3,1,2]
# start = 0
arr = [3,0,2,1,2] 
start = 2

sol = Solution()
print(sol.can_reach(arr, start))