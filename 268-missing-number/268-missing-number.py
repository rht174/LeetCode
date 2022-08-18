class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ls = [-1] * (len(nums)+1)
        for i in nums:
            ls[i] = i
        return ls.index(-1)
        