from typing import *

class Solution:
    def dfs(self, grid: List[List[str]],i:int,j:int):
        if i<0 or i>= len(grid) or \
            j<0 or j>= len(grid[0]) or \
            grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'

        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count+=1
        return count


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
res = Solution()
print(res.numIslands(grid))