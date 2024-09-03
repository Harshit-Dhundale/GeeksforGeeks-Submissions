#User function Template for python3

from typing import List

class Solution:
    def dfs(self, node, d, ans, sset):
        if node in sset: return
        sset.add(node)
        for nei in d.get(node, []):
            self.dfs(nei, d, ans, sset)
        
        ans.append(node)
        
    
    def findOrder(self, ls: List[str], n: int, k: int) -> str:
        d = dict()
        for i in range(k): d[i] = []
        for i in range(len(ls) - 1):
            a, b = ls[i], ls[i + 1]
            for j in range(len(a)):
                if j == len(b): break
                if a[j] != b[j]:
                    d[ord(b[j]) - 97].append(ord(a[j]) - 97)
                    break
        
        ans, sset = [], set()
        
        for i in range(k):
            self.dfs(i, d, ans, sset)
        
        return ''.join([chr(97 + x) for x in ans])



#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends