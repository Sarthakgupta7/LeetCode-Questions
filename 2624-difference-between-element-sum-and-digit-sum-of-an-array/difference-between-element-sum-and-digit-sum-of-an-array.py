class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s,d=0,0
        for i in nums:
            s+=i
            for j in str(i):
                d+=int(j)
        return(abs(s-d))
        