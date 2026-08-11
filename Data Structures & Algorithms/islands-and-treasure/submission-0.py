class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols= len(grid), len(grid[0])
        path=set()
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    path.add((r,c))
        step=0
        while q:
            step+=1
            for i in range(len(q)):

                r,c= q.popleft()
                directions=[(-1,0), (1,0), (0,-1), (0, 1)]

                for dr, dc in directions:

                    nr, nc= r+dr, c+dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        (nr,nc) not in path and
                        grid[nr][nc]==2147483647):
                        q.append((nr, nc))
                        path.add((nr, nc))
                        grid[nr][nc]=step


                


            
