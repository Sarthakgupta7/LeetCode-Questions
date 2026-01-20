class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=[]
        for i in range(len(nums)):
            o=0
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    o+=1
            s.append(o)
        return s
        