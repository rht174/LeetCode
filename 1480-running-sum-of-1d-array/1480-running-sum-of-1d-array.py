class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = []
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            x.append(count)
        return x