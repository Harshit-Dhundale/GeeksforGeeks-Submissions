#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
            def maxPathSum(self, arr1, arr2):
                i,j,n1,n2,curr1,curr2,ans=0,0,len(arr1),len(arr2),0,0,0
                while i<n1 and j<n2:
                    if arr1[i]==arr2[j]:
                        ans+=max(curr1,curr2)
                        ans+=arr1[i]
                        curr1,curr2=0,0
                        i+=1
                        j+=1
                    elif arr1[i]<arr2[j]:
                        curr1+=arr1[i]
                        i+=1
                    else:
                        curr2+=arr2[j]
                        j+=1
                while i<n1:
                    curr1+=arr1[i]
                    i+=1
                while j<n2:
                    curr2+=arr2[j]
                    j+=1
                ans+=max(curr1,curr2)
                return ans
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends