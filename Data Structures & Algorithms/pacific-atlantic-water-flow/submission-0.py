class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = [[False]* cols for _ in range(rows)]
        atl = [[False]* cols for _ in range(rows)]
        pacific =[]
        atlantic =[]
        directions =[[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(source, ocean):
            q = collections.deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
            
                for rd, cd in directions:
                    nr, nc = r+rd, c+cd
                    if (nr>=0 and nr<rows and nc>=0 and nc<cols and
                       not ocean[nr][nc] and 
                       heights[nr][nc] >=heights[r][c]  ):
                       ocean[nr][nc] = True
                       q.append((nr, nc))



        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols-1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res =[]
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res



        