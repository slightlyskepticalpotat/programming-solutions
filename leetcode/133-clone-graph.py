"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        adj, queue = {node: Node(node.val)}, collections.deque([node])
        while queue:
            cur = queue.popleft()
            for peer in cur.neighbors:
                if peer not in adj: # add to our hashmap
                    adj[peer] = Node(peer.val)
                    queue.append(peer)
                adj[cur].neighbors.append(adj[peer])
        return adj[node]