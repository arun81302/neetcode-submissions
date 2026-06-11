class Solution:
    def getConcatenation(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*(n+n)
        for i in range(len(arr)):
            res[i]=arr[i]
            res[i+n]=arr[i]
        return res
        