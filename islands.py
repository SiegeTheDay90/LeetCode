from collections import deque
import pdb
class Solution:
    def numIslands(self, grid) -> int:
        union_find = [num for num in range(len(grid)*len(grid[0]))]
        unique_parents = set()
        max_x = len(grid) - 1
        max_y = len(grid[0]) - 1

        for i in range(len(union_find)):
            x = i//(len(grid[0]))
            y = i%len(grid[0])

            if grid[x][y] == "0":
                union_find[i] = None

            elif grid[x][y] == "1":
                if x+1 <= max_x and grid[x+1][y] == "1":
                    self.union(union_find, i, i+len(grid[0]))
                if y+1 <= max_y and grid[x][y+1] == "1":
                    self.union(union_find, i, i+1)
                if x-1 >= 0 and grid[x-1][y] == "1":
                    self.union(union_find, i, i-len(grid[0]))
                if y-1 >= 0 and grid[x][y-1] == "1":
                    self.union(union_find, i, i-1)

        for i in union_find:
            if i != None:
                unique_parents.add(i)

        return len(unique_parents)

    def find(self, uf, num):
        while uf[num] != num:
            num = uf[num]
        return num
    
    def union(self, uf, parent, child):
        uf[self.find(uf, child)] = self.find(uf, parent)
        

s = Solution()

print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))
print(s.numIslands([["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]))