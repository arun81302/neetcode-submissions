class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        space=False
        for i in range(len(s)-1,-1,-1):
            if space==True:
                break
            elif s[i]!=' ':
                count+=1
            elif count>0 and s[i]==' ':
                space=True
        return count
        