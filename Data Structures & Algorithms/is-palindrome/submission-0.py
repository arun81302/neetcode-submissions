class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        clean=""
        for ch in s:
            if ch.isalnum():
                clean+=ch
        i=0
        j=len(clean)-1
        while i<j:
            if clean[i]!=clean[j]:
                return False
            i+=1
            j-=1
        return True
        