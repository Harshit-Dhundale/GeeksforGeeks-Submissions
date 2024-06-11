#User function Template for python3
class Solution:
	def timeToWord(self, H, M):
		# code here
		trans = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'}
        
        if M==0:
            return "{} o' clock".format(trans[H])
        elif 0<M<15 or 15<M<30:
            return "{} {} past {}".format(trans[M], "minute" if M==1 else "minutes", trans[H])
        elif M==15:
            return "quarter past {}".format(trans[H])
        elif M==30:
            return "half past {}".format(trans[H])
        elif M==45:
            return "quarter to {}".format(trans[H+1])
        elif 30<M<45 or 45<M<60:
            return "{} {} to {}".format(trans[60-M],"minute" if 60-M==1 else "minutes", trans[H+1])
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		H,M = input().split()
		H=int(H)
		M=int(M)
		ob = Solution();
		print(ob.timeToWord(H,M))

# } Driver Code Ends