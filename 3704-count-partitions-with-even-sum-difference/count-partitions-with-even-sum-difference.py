class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        o,l=0,len(nums)
        for i in range(1,l):
            diff=abs(sum(nums[:i])-sum(nums[i:l]))
            if(diff%2==0):
                o+=1
        return o


        