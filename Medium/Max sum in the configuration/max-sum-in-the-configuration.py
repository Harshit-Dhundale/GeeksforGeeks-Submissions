#User function Template for python3
def max_sum(a,n):
    #code here
    # postfix sum
    post=[a[-1]]
    for i in range(n-2,-1,-1):
        post.append(post[-1]+a[i])
    
    
    post.reverse()
    ans=0
    #prefix sum
    pre=[a[0]]
    for i in range(1,n):
        pre.append(pre[-1]+a[i])
        ans+=(i*a[i])
    pre.append(0)
    res=ans
    for i in range(1,n):
        #netchange..
        ans-=(post[i]+pre[i-2])
        ans+=(a[i-1]*(n-1))
        res=max(res,ans)
    return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends