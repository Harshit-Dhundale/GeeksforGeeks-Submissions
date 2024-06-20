# Your task is to complete all these function's
def push(arr, ele):
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    if arr:
        return arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    return len(arr) == n

# function should return 1/0 or True/False
def isEmpty(arr):
    if arr:
        return False
    return True

# function should return minimum element from the stack
def getMin(n, arr):
    min = arr[0]
    for num in arr:
        if num < min:
            min = num
    return min

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while(not isEmpty(stack)):
            pop(stack)
            
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends