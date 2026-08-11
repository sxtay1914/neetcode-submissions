class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        # Create adjacency list
        adjList = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        count = 0
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            visit.add(node)
            for neighbour in adjList[node]:
                if neighbour not in visit:
                    dfs(neighbour)
            return True 

        # Iterate through each node
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count

        