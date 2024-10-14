class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # make a adj list
        # do dfs on adj list to find if there are any cycles
        # check if total no of visited nodes are equal to n
        if not n:
            return True
        
        adj = collections.defaultdict(list)
        # create adj list
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        print(adj)

        # dfs
        visited = set()
        def dfs(i, prev):
            # detect loop
            if i in visited:
                return False
            
            visited.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                
                if not dfs(nei, i):
                    return False
            return True
        
        
        if dfs(0, -1) and n == len(visited):
            return True
        else:
            return False