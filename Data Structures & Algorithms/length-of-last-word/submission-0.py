class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=s.strip()
        arr=list(s)
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==" ":
                break
            count+=1
        return count
        