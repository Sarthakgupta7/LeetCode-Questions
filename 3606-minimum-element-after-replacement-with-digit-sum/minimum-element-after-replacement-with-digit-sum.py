class Solution:
    def minElement(self, nums: List[int]) -> int:

        for i in range(len(nums)):
                s=0
                n = nums[i]
                a,b,c,d,e = n % 10,(n // 10) % 10,(n // 100) % 10,(n // 1000) % 10,(n // 10000) % 10
                s=a+b+c+d+e
                nums[i]=s
        return min(nums)