class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {i: [] for i in range(n)} 
        for edge in edges:
            edgeMap[edge[0]].append(edge[1])
            edgeMap[edge[1]].append(edge[0])

        visited = set()
        count = 0
        def dfs(prev,n):
            if n in visited :
                return False

            visited.add(n)
            for edge in edgeMap[n]:
                dfs(n, edge)

            return True


        for i in range(n):
            if not edgeMap[i]:
                count += 1
            else:
                if dfs(-1,i):
                    count += 1

        return count