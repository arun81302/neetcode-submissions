class Solution:
    def findMaxConsecutiveOnes(self, arr: List[int]) -> int:
        count=0
        maxcount=0
        for i in arr:
            if i==1:
                count+=1
                maxcount=max(count,maxcount)
            if i==0:
                count=0
        return maxcount
        