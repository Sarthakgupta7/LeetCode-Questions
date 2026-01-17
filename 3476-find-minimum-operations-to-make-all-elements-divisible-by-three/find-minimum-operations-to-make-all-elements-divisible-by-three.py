class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l=len(nums)
        k=0
        for i in nums:
            if(i%3==0):
                k+=1
        return l-k