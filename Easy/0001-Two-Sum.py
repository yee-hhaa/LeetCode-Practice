class Solution(object):
    def twoSum(self, nums, target):
        """
        思路：Hash Map 存已遍歷的數字，O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i
