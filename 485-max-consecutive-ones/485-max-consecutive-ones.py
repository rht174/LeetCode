class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        maxx = 0
        for i in nums:
            if i == 1:
                maxx += 1
                ans = max(maxx, ans)
            else:    
                maxx = 0
            
        return ans