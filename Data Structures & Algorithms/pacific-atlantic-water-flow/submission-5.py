from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        bfs from atlantic -> store in dict

        bfs from pacific -> append to answer if in dict
        '''
        ROWS = len(heights)
        COLS = len(heights[0])
        output = []
        dirs= ((0,1),(0,-1),(1,0),(-1,0))

        pacific = set() #marks ones we could reach
        visit = set()
        q = deque()
        # branch out from pacific first
        for r in range(1, ROWS):
            q.append((r,0))
            visit.add((r,0))
        for c in range(COLS):
            q.append((0,c))
            visit.add((0,c))
        
        # bfs
        while q:
            cr, cc = q.popleft()

            for dr,dc in dirs:
                nr,nc = cr+dr, cc+dc
                # only go if goes up or flat
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visit and heights[nr][nc] >= heights[cr][cc]:
                    q.append((nr,nc))
                    visit.add((nr,nc))
                    

        # move it
        pacific = visit.copy()
        visit.clear()

        # bfs from atlantic. q is cleared
        for r in range(ROWS-1):
            q.append((r, COLS-1))
            visit.add((r, COLS-1))
        for c in range(COLS):
            q.append((ROWS-1, c))
            visit.add((ROWS-1, c))
        #print(q)
        #print(pacific)
        while q:
            cr, cc = q.popleft()
            
            if (cr,cc) in pacific:
                # visited during the prev run
                output.append([cr,cc])
            for dr,dc in dirs:
                nr,nc = cr+dr, cc+dc
                # only go if goes up or flat
                # only go if goes up or flat
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visit and heights[nr][nc] >= heights[cr][cc]:               
                    visit.add((nr,nc))
                    q.append((nr,nc))
                    # add to visit now so it dont happen twice

        return output