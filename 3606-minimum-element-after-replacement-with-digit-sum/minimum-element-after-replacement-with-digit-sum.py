class Solution:
    def minElement(self, nums: List[int]) -> int:

        for i in range(len(nums)):
                a,b,c,d,e = nums[i] % 10,(nums[i] // 10) % 10,(nums[i] // 100) % 10,(nums[i] // 1000) % 10,(nums[i] // 10000) % 10
                nums[i]=a+b+c+d+e
        return min(nums)