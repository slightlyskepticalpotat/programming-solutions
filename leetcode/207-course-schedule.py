class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj, visited = [[] for i in range(numCourses)], [0 for i in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        def cycle(node):
            if visited[node] == -1: # cyclic dependency
                return True
            elif visited[node] == 1: # dependency satisfied
                return False
            visited[node] = -1
            if any(cycle(peer) for peer in adj[node]): 
                return True
            visited[node] = 1
            return False
        return not any(cycle(i) for i in range(numCourses))