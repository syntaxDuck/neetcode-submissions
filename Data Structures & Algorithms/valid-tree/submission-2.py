class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        treeMap = {i: [] for i in range(n)}
        for edge in edges:
            treeMap[edge[0]].append(edge[1])
            treeMap[edge[1]].append(edge[0])

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            if not treeMap[node]:
                return True

            for edge in treeMap[node]:
                if edge == prev:
                    continue
                    
                if not dfs(edge, node):
                    return False

            treeMap[node] = []
            return True

        if not dfs(0, -1):
            return False

        if len(visited) != n:
            return False

        return True