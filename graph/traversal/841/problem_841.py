'''
#dfs

There are n rooms labeled from 0 to n - 1 and all the rooms are locked
except for room 0. Your goal is to visit all the rooms. However, you
cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each
key has a number on it, denoting which room it unlocks, and you can take
all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can
obtain if you visited room i, return true if you can visit all the
rooms, or false otherwise.

Input: rooms = [[1],[2],[3],[]] Output: true

Input: rooms = [[1,3],[3,0,1],[2],[0]] Output: false
'''


class Solution:

    def dfs_approach(self, rooms: list[list[int]]) -> bool:
        print("[DFS]")

        visited = [False for _ in range(len(rooms))]

        def dfs(cur_room: int) -> None:
            for next_room in rooms[cur_room]:
                if not visited[next_room]:
                    visited[next_room] = True
                    dfs(next_room)

        start_room = 0
        visited[start_room] = True
        dfs(start_room)

        return all(room == True for room in visited)
