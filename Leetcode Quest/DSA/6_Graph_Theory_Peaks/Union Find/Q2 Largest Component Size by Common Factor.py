"""
Largest Component Size by Common Factor

You are given an integer array of unique positive integers nums. Consider the following graph:

There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:


Input: nums = [4,6,15,35]
Output: 4
Example 2:


Input: nums = [20,50,9,63]
Output: 2
Example 3:


Input: nums = [2,3,6,7,4,12,21,39]
Output: 8
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 105
All the values of nums are unique.


"""

from typing import List
from collections import defaultdict

class DisJointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]
    
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x==root_y:
            return 
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        res = 0
        ds = DisJointSet(max(nums)+1)
        mpp = defaultdict(int)

        for num in nums:
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    ds.union(num,i)
                    ds.union(num,num//i)

        for num in nums:
            root = ds.find(num)
            mpp[root]+=1
            res = max(res,mpp[root])
        return res 