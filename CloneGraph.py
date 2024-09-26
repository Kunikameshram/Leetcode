"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNewMap = {}

        def clone(node):
            if node in oldNewMap:
                return oldNewMap[node]
            
            c = Node(node.val)
            oldNewMap[node] = c
            
            for adjacent in node.neighbors:
                c.neighbors.append(clone(adjacent))
            return c

        return clone(node) if node else None
