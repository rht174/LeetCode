class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l1 = []
        d1 = {}.fromkeys((range(1, len(nums)+1)), 0)
        for item in nums:
            d1[item] += 1
            if d1[item] > 1:
                l1.append(item)
        return l1