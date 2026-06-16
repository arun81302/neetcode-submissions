class Solution:
    def countSeniors(self, arr: List[str]) -> int:
        count=0
        s=0
        for i in arr:
            value=0
            s=i[11:13]
            s=int(s)
            if s>60:
                count+=1
        return count
        