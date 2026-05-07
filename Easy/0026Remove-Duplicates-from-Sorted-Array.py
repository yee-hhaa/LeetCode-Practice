class Solution(object):
    def removeDuplicates(self, nums):
        """
        思路：Two Pointer，i 追蹤不重複區域的末端，j 往前掃描，遇到新數字就放到 i+1 的位置
        :type nums: List[int]
        :rtype: int
        """
        
        k = 1
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                k += 1
        return k
        
