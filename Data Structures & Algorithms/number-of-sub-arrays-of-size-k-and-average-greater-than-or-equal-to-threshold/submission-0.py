class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        maxsum=sum(arr[0:k])
        sumvalue=maxsum
        if sumvalue/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            maxsum=maxsum+arr[i]-arr[i-k]
            average=maxsum/k
            if average>=threshold:
                count+=1
        return count
        