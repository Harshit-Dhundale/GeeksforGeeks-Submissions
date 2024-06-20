#User function Template for python3
class Solution:
  def findKRotation(self,arr,  n):
        start,end=0,n-1
        mid=0
        last_ele=arr[n-1]
        while(start<=end):
            mid=start+(end-start)//2
            if(arr[mid]<=last_ele):
                if(mid-1<0 or arr[mid-1]>arr[mid]):
                    return mid
                end=mid
            else:
                start=mid+1
        return mid
        # code here
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends