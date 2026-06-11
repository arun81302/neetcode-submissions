class Solution:
    def scoreOfString(self, s: str) -> int:
        sumvalue=0
        for i in range(1,len(s)):
            sumvalue+=abs(ord(s[i])-ord(s[i-1]))
        return sumvalue
        