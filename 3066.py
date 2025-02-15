from heapq import heapify, heappush, heappop
class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        ans = 0
        while len(nums)>1 and nums[0]<k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            insert = min(x,y)*2 + max(x,y)
            heapq.heappush(nums,insert)
            ans+=1
        return ans
        
'''
https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/
You are given a 0-indexed integer array nums, and an integer k.

You are allowed to perform some operations on nums, where in a single operation, you can:

Select the two smallest integers x and y from nums.
Remove x and y from nums.
Insert (min(x, y) * 2 + max(x, y)) at any position in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
'''