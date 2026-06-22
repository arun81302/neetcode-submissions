class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if arr[i]<0:
                arr[i]=arr[i]*(-1)
        for i in range(len(arr)):
            arr[i]=arr[i]*arr[i]
        arr.sort()
        return arr
        