class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d1 = {}.fromkeys((range(1, len(nums)+1)), 0)
        for i in nums:
            d1[i] += 1
            if d1[i] == 2:
                return i