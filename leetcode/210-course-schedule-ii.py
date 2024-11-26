class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def toposort(graph):
            searched, stack = set(), []
            for node in graph:
                if node not in searched:
                    toposort_recurse(graph, node, searched, stack)
            return stack[::-1]

        def toposort_recurse(graph, node, searched, stack):
            searched.add(node)
            for peer in graph[node]:
                if peer not in searched:
                    toposort_recurse(graph, peer, searched, stack)
            stack.append(node)
        
        graph = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            graph[j].append(i)
        path = toposort(graph)
        if any(path.index(peer) < path.index(node) for node in graph for peer in graph[node]):
            path = []
        return path