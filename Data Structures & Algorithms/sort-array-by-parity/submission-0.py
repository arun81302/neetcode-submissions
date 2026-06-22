class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*n
        i=0
        for j in arr:
            if j%2==0:
                res[i]=j
                i+=1
        for j in arr:
            if j%2!=0:
                res[i]=j
                i+=1
        return res

        