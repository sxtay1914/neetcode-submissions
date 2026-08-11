class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
             return True
        adjList={c:[] for c in range(n)}

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit=set()

        def dfs(n, prev):
            if n in visit:
                return False
            visit.add(n)
            for neighbour in adjList[n]:
                if neighbour==prev:
                    continue
                if not dfs(neighbour, n):
                    return False
            return True
        #check cycle and connections of nodes
        return  dfs(0, -1) and len(visit)==n 