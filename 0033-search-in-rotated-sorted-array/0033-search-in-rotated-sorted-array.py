class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(arr):
            start = 0
            end = len(arr) - 1
            if arr[start] < arr[end]:
                return -1
            while start <= end:
                mid = start + (end - start) // 2
                if start == mid and mid == end:
                    return mid
                if mid != end and arr[mid] > arr[mid + 1]:
                    return mid
                if mid != end and arr[mid] < arr[mid - 1]:
                    return mid - 1
                if arr[mid] > arr[start]:
                    start = mid + 1
                else:
                    end = mid -1
            return -1
        
        def binary_search(arr, start, end, target):
            while start <= end:
                mid = start + (end - start) // 2
                if target == arr[mid]:
                    return mid
                elif target > arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        pivot = find_pivot(nums)
        print(pivot)

        if pivot == -1:
            return binary_search(nums, 0, len(nums) - 1, target)

        if target == nums[pivot]:
            return pivot

        elif target >= nums[0]:
            return binary_search(nums, 0, pivot, target)

        else:
            return binary_search(nums, pivot + 1, len(nums) - 1, target)
                    