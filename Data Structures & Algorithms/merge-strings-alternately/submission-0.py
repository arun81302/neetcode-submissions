class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        s=""
        i=0
        j=0
        while i<len(a) and j<len(b):
            s+=a[i]
            i+=1
            s+=b[j]
            j+=1
        if i<len(a):
            while i<len(a):
                s+=a[i]
                i+=1
        if j<len(b):
            while j<len(b):
                s+=b[j]
                j+=1
        return s
        
        