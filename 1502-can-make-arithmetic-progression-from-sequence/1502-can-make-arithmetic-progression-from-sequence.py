class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        arr.sort()
        for i in range(2, len(arr)):
            if arr[i-1] - arr[i-2] == arr[i-0] - arr[i-1]:
                continue
            else:
                return False
        return True