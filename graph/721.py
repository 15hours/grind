'''
#dsu, #dfs, #dict

Given a list of accounts where each element accounts[i] is a list of 
strings, where the first element accounts[i][0] is a name, and the rest 
of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely 
belong to the same person if there is some common email to both 
accounts. Note that even if two accounts have the same name, they may 
belong to different people as people could have the same name. A person 
can have any number of accounts initially, but all of their accounts 
definitely have the same name.

After merging the accounts, return the accounts in the following 
format: the first element of each account is the name, and the rest of 
the elements are emails in sorted order. The accounts themselves can be 
returned in any order.

 

Example 1:
Input: accounts = [["John","johnsmith@mail.com",
                                        "john_newyork@mail.com"],
                    ["John","johnsmith@mail.com","john00@mail.com"],
                    ["Mary","mary@mail.com"],
                    ["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com",
                                        "johnsmith@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common 
email "johnsmith@mail.com".
The third John and Mary are different people as none of their email 
addresses are used by other accounts.
We could return these lists in any order, for example the answer 
[['Mary', 'mary@mail.com'], 
['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 
                            'johnsmith@mail.com']] 
would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
'''
import collections


class UnionFind:
    def __init__(self, num_accounts: int) -> None:
        self.root = list(range(num_accounts))
        self.rank = [1 for _ in range(num_accounts)]

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node_1: int, node_2: int) -> None:
        root_node_1 = self.find(node_1)
        root_node_2 = self.find(node_2)

        if root_node_1 != root_node_2:
            if self.rank[root_node_1] < self.rank[root_node_2]:
                self.root[root_node_1] = self.root[root_node_2]
                self.rank[root_node_2] += self.rank[root_node_1]
            else:
                self.root[root_node_2] = self.root[root_node_1]
                self.rank[root_node_1] += self.rank[root_node_2]


class Solution:

    def _dsu_approach(self, 
                            accounts: list[list[str]]
                            ) -> list[list[str]]:
                            
        uf = UnionFind(len(accounts))
        ownership = dict()
        
        for owner, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(ownership[email], owner)
                else:
                    ownership[email] = owner
        
        merged_emails = collections.defaultdict(list)
        for email, owner in ownership.items():
            merged_emails[uf.find(owner)].append(email)

        answer = []
        for owner, emails in merged_emails.items():
            answer.append([accounts[owner][0]] + sorted(emails))

        return answer

    def _dfs_approach(self, 
                      accounts: list[list[str]]
                      ) -> list[list[str]]:
        visited = [False for _ in range(len(accounts))]
        adj_list = collections.defaultdict(list)
        for owner, (_, *emails) in enumerate(accounts):
            for email in emails:
                adj_list[email].append(owner)

        def dfs(acc_id, nodes: set[int]) -> None:
            if visited[acc_id]:
                return
            
            visited[acc_id] = True
            for i in range(1, len(accounts[acc_id])):
                cur_node = accounts[acc_id][i]
                if cur_node in nodes:
                    continue

                nodes.add(cur_node)
                for next_acc_id in adj_list[cur_node]:
                    dfs(next_acc_id, nodes)

        answer = []
        for owner in range(len(accounts)):
            if visited[owner]:
                continue
            emails = set()  
            dfs(owner, emails)
            answer.append([accounts[owner][0]] + sorted(emails))

        return answer

    def accounts_merge(self, 
                       accounts: list[list[str]]
                       ) -> list[list[str]]:
        return self._dsu_approach(accounts)
        # return self._dfs_approach(accounts)
    
    
sol = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
# accounts = [["David","David0@m.co","David1@m.co"],
#             ["David","David3@m.co","David4@m.co"],
#             ["David","David4@m.co","David5@m.co"],
#             ["David","David2@m.co","David3@m.co"],
#             ["David","David1@m.co","David2@m.co"]]
print(sol.accounts_merge(accounts))