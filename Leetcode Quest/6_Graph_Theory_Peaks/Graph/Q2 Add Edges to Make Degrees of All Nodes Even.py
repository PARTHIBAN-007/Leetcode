"""
Add Edges to Make Degrees of All Nodes Even

There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.
You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.
Return true if it is possible to make the degree of each node in the graph even, otherwise return false.
The degree of a node is the number of edges connected to it.

 

Example 1:


Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
Output: true
Explanation: The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.
Example 2:


Input: n = 4, edges = [[1,2],[3,4]]
Output: true
Explanation: The above diagram shows a valid way of adding two edges.
Example 3:


Input: n = 4, edges = [[1,2],[1,3],[1,4]]
Output: false
Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.
 

Constraints:

3 <= n <= 105
2 <= edges.length <= 105
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There are no repeated edges.
"""
from typing import List
from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        odd_nodes = []
        for i in range(1,n+1):
            if len(graph[i])%2==1:
                odd_nodes.append(i)
        
        if not odd_nodes:
            return True
        if len(odd_nodes)==2:
            a,b = odd_nodes
            if b not in graph[a]:
                return True
            for x in range(1,n+1):
                if x!=a and x!=b:
                    if x not in graph[a] and x not in graph[b]:
                        return True
            return False
        if len(odd_nodes)==4:
            a,b,c,d  = odd_nodes
            pairs = [
                (a,b,c,d),
                (a,c,b,d),
                (a,d,b,c)
            ]

            for x1,y1,x2,y2 in pairs:
                if y1 not in graph[x1] and y2 not in graph[x2]:
                    return True
        return False