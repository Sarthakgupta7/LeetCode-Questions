class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]==nums[j] and i<j):
                    s+=1
        return s

        