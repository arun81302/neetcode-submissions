class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxvalue=float('-inf')
        for i in range(len(arr)-1,-1,-1):
            cur=arr[i]
            maxvalue=max(maxvalue,cur)
            arr[i]=maxvalue
        arr.pop(0)
        arr.append(-1)
        return arr
        