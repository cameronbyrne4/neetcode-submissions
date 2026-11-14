"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # im assuming this is a bfs or dfs? doesnt really matter as long as im not going in circles
        
        # Graph is empty or size 1
        if not node:
            return None
        
        # dfs
        clones = [None] * 101
        def dfs(node):
            if clones[node.val]: #means that index has neighbors
                return clones[node.val]

            # if it hasn't been cloned, we need to clone it
            clone = Node(node.val)
            clones[node.val] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)

        