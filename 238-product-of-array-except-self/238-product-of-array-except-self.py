class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = [0] * len(nums)
        ap = 1
        
        if nums == x or nums.count(0) > 1:
            return x
        
        for i in nums:
            if i == 0:
                continue
            ap *= i
            
        if nums.count(0) == 1:
            for i, j in enumerate(nums):
                if j == 0:
                    x[i] = ap
            return x
                
        for i,j in enumerate(nums):
            x[i] = ap // j
        return x