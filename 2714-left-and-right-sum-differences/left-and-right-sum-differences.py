class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ts= sum(nums)
        ls = 0
        ans = []

        for num in nums:
            rs= ts - ls - num
            ans.append(abs(ls- rs))
            ls+= num

        return ans


        