def binaryNextNumber(self, s):
        i = int(s,2)
        return str(bin(i+1))[2:]
