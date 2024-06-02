from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        mpp = {}
        ans = [0]
        for i in range(q):
            qtype = queries[i][0]
            qval  = queries[i][1]
            if qtype == 0:
                ans.append(qval)
            else:
                ind = len(ans)-1
                if ind in mpp.keys():
                    mpp[ind] ^= qval
                else:
                    mpp[ind] = qval
        n = len(ans)
        xorVal = 0
        for i in range(n-1, -1, -1):
            if i in mpp.keys():
                xorVal ^= mpp[i]
            ans[i] ^= xorVal
        return sorted(ans)
                                # TC = O(q.logq) SC = O(q)
