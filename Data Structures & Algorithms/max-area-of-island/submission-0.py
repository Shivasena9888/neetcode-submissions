class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid :
            return 0
        areaMax =0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def bfs(r, c):
            q= collections.deque()
            visit.add((r, c))
            q.append((r,c))
            area =1

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for rd , cd in directions:
                    r,c  = row+rd, col+cd
                    if ( r in range(rows) and
                     c in range(cols) and
                     grid[r][c] == 1 and
                     (r, c) not in visit):
                     visit.add((r, c))
                     q.append((r,c))
                     area += 1
            return area

                

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and (r, c) not in visit):
                    areaMax = max(areaMax, bfs(r, c))
        return areaMax
                     

        