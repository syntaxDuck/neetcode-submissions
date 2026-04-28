"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        root = Node()
        visited = {}
        def dfs(source, target):
            if not len(source.neighbors) or source.val in visited:
                return

            target.val = source.val
            visited[source.val] = target
            for neighbor in source.neighbors:
                if neighbor.val in visited:
                    target.neighbors.append(visited[neighbor.val])
                else:
                    target.neighbors.append(Node(neighbor.val))
                    dfs(neighbor, target.neighbors[-1])

        dfs(node, root)
        return root