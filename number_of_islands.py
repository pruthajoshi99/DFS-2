#TC - O(m*n)
# Sc - O(m*n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == None or len(grid[0]) == None:
            return 0

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        count = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append((i,j))
                    grid[i][j] = '-1'
                    count+=1
                    while len(queue)!=0:
                        ii,jj=queue.popleft()
                        for r,c in dirs:
                            newr, newc= ii+r, jj+c
                            if (newr>=0 and newr<m) and (newc >=0 and newc<n) and grid[newr][newc] == '1':
                                queue.append((newr,newc))
                                grid[newr][newc] = '-1'
        return count                        

        
