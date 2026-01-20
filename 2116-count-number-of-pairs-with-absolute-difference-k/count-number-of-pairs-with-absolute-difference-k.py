class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        o=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(abs(nums[i]-nums[j])==k):
                 o+=1
        return o