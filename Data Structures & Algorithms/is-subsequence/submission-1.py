class Solution:
    def isSubsequence(self, a: str, b: str) -> bool:
        i=0
        j=0
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==len(a):
            return True
        return False
        