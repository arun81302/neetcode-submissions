class Solution:
    def minimumDifference(self, arr: List[int], k: int) -> int:
        arr.sort()
        minans=float('inf')
        i=0
        j=k
        while j<=len(arr):
            brr=arr[i:j]
            maxvalue=max(brr)
            minvalue=min(brr)
            result=maxvalue-minvalue
            minans=min(minans,result)
            i+=1
            j+=1
        return  minans
                

        