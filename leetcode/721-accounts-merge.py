from collections import defaultdict

class Solution:
    def dfs(self, node):
        self.visited.add(node)
        for peer in self.graph[node]:
            if peer not in self.visited:
                self.dfs(peer)
        self.cur.append(node)
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.graph = defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                self.graph[account[1]].add(email) # we can also use union-find
                self.graph[email].add(account[1])
        self.visited, ans = set(), []
        for account in accounts:
            for email in account[1:]:
                if email not in self.visited:
                    self.cur = []
                    self.dfs(email)
                    ans.append([account[0]] + sorted(self.cur))
        return ans