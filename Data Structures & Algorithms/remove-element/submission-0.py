class Solution:
    def removeElement(self, arr: List[int], k: int) -> int:
        i=j=0
        while j<len(arr):
            if arr[i]!=k and arr[j]!=k:
                i+=1
                j+=1
            elif arr[i]==k and arr[j]==k:
                j+=1
            elif arr[i]==k and arr[j]!=k:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j+=1
        return i
        