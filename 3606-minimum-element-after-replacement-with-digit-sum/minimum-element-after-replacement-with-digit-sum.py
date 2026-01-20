class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = 0
            for d in str(nums[i]):
                s += int(d)
                nums[i]=s
        return min(nums)