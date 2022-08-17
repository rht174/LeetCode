class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d1 = {}.fromkeys(nums, 0)
        for i in nums:
            d1[i] += 1
        for x,y in d1.items():
            if y==1:
                return x