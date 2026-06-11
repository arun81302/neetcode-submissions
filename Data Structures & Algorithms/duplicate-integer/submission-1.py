class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        seen=set(arr)
        if len(seen)!=len(arr):
            return True
        return False
        
        