class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d1 = {}.fromkeys(nums, 0)
        for i in nums:
            d1[i] += 1
            if d1[i] >= 2:
                return True
        return False
    
