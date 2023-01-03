#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
		start = 0
		end = n - 1
		
		while start < end:
		    mid = start + (end - start) // 2
		    if arr[mid] > arr[mid + 1]:
		        end = mid
		    else:
		        start = mid + 1
		        
		return arr[start]


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends