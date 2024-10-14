class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        nodes = list(range(n))
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        print(adj)

        visited = set()
        def dfs(i):
            visited.add(i)

            for nei in adj[i]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        count = 0
        for i in nodes:
            if i in visited:
                continue
            count += 1
            dfs(i)