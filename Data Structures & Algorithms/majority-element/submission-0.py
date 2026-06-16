class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        cand=-1
        count=0
        for i in range(len(arr)):
            if count==0:
                cand=arr[i]
            if arr[i]==cand:
                count+=1
            else:
                count-=1
        count=0
        for i in arr:
            if i==cand:
                count+=1
        if count>len(arr)/2:
            return cand
            
        