class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        dic1 = {}.fromkeys(range(1, len(nums)+1), 0)
        for i in nums:
            dic1[i] += 1
            
        for key, value in dic1.items():
            if value == 0:
                ans.append(key)
        
        return ans