from collections import defaultdict
import pdb

class UnionFind:
    def __init__(self, size):
        self.union_find = [num for num in range(0, size)]
        
    def union(self, parent, child):
        self.union_find[child] = self.root(self.union_find[parent])

    def root(self, node):
        while node != self.union_find[node]:
            node = self.union_find[node]
        
        return node

    def max_size(self):
        counts = defaultdict(lambda: 0)

        for node in self.union_find:
            counts[self.root(node)] += 1

        pdb.set_trace()
        return max(counts.values())

class Solution:
    def longestConsecutive(self, nums) -> int:

        union_find = UnionFind(len(nums))
        visited = set()
        indices = dict()

        for i in range(0, len(nums)):
            num = nums[i]
            if num in visited:
                continue
            indices[num] = i

            if num+1 in visited:
                union_find.union(indices[num+1], i)
            if num-1 in visited:
                union_find.union(i,indices[num-1])
            visited.add(num)

        return union_find.max_size()
    
s = Solution()

print(s.longestConsecutive([100,4,200,1,3,2]))


