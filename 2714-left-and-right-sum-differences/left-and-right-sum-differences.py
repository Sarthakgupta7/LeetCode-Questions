class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls,rs=0,0
        k=[]
        for i in range(len(nums)):
           ls=sum(nums[i+1:])
           rs=sum(nums[:i])
           k.append(abs(ls-rs))
        return k


        