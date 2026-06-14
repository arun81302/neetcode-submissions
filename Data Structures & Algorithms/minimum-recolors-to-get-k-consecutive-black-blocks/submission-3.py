class Solution:
    def minimumRecolors(self, arr: str, k: int) -> int:
        mincount=float('inf')
        count=0
        brr=arr[0:k]
        for ch in brr:
            if ch=='W':
                count+=1
        mincount=min(mincount,count)
        i=1
        j=k
        while j<len(arr):
            if arr[j]=='W':
                count+=1
            if arr[i-1]=='W':
                count-=1
            mincount=min(mincount,count)
            i+=1
            j+=1
        return mincount
        