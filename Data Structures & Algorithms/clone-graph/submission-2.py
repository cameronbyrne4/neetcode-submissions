"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

- reading adj list via bfs,
- creating nodes and appending to their lists as we go on?
- so if it's not in visited, we will create the new object?

Should we build it as we go or just make more objects at the end?

Track made objects in dict # ID -> Node obj
"""
from collections import deque, defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # Todo, edge case for empty input
        q = deque()
        objs = defaultdict(Node)    # int -> Node
        #visit = set()
        q.append(node)
        #visit.add(1)    # node.val for the root
        
        # create deep initial node now
        
        newNode = Node(node.val)
        objs[1] = newNode

        while q:
            curNode = q.popleft()

            for neiNode in curNode.neighbors:
                # check visited always

                # First time seeing this value ever --> make new object
                if neiNode.val not in objs: # vals are the new
                    newNode = Node(neiNode.val)
                    objs[neiNode.val] = newNode

                    # visit.add(neiNode.val)
                    q.append(neiNode)
                
                # now connect objs to the adj list in our new links
                print(f"connecting nei and cur = {neiNode.val}, {curNode.val}")
                objs[curNode.val].neighbors.append(objs[neiNode.val])
                # objs[neiNode.val].neighbors.append(objs[curNode.val])
                    # this step happens when we are working on that node

        return objs[1]  # holds the first node of the dopy













