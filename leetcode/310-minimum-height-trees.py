from collections import defaultdict

class Solution: # midpoint/midpoints of longest path or remove leaves until 1-2 left
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(set)
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [node for node in adj if len(adj[node]) == 1]
        while n > 2:
            n, next_leaves = n - len(leaves), []
            for leaf in leaves:
                parent = adj[leaf].pop() # remove them from graph
                adj[parent].remove(leaf)
                if len(adj[parent]) == 1:
                    next_leaves.append(parent)
            leaves = next_leaves
        return leaves