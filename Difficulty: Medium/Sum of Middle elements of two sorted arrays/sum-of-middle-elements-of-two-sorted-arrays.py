#User function Template for python3
class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        arr1.extend(arr2)
        arr1.sort()
        low = 0
        high = len(arr1)-1
        mid = (low + high)//2
        
        return arr1[mid]+ arr1[mid+1]# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends