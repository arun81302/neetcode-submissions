class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        count=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                count+=customers[i]
                customers[i]=0
        k=minutes
        windowsum=sum(customers[0:k])
        maxsum=windowsum
        for i in range(k,len(customers)):
            windowsum=windowsum+customers[i]-customers[i-k]
            maxsum=max(maxsum,windowsum)
        return maxsum+count
        