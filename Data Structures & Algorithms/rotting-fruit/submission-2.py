class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        q= collections.deque()
        visit = set()
        count =0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==2:
                    q.append((r, c))
                    visit.add((r, c))
                if grid[r][c] ==1 :
                    count += 1

        minutes =0

        def rot(r, c):
            if (r<0 or c<0 or r==rows or c==cols or 
                (r, c) in visit or grid[r][c] != 1):
                return 
            grid[r][c] +=1
            nonlocal count
            count -=1
            q.append((r, c))
            visit.add((r, c))

        while q and count:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)
            minutes +=1
            if count ==0:
                return minutes
        return minutes if count ==0 else -1


        