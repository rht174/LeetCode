class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ls = [0] * max(max(nums), len(nums))
        for i in nums:
            ls[i-1] = i
        x = []
        for a,b in enumerate(ls):
            if b == 0:
                x.append(a+1)
        return x
            
            