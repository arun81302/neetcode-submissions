class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        aseen={}
        bseen={}
        for i in a:
            if i in aseen:
                aseen[i]+=1
            else:
                aseen[i]=1
        for i in b:
            if i in bseen:
                bseen[i]+=1
            else:
                bseen[i]=1
        return aseen==bseen
        