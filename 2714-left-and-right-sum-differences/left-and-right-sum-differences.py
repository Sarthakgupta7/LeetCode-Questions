class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # ls,ts=0,sum(nums)
        # k=[]
        # for i in range(len(nums)):
        #    ls=sum(nums[i+1:])
        #    k.append(abs(ls-(ts-ls-nums[i])))
        # return k
        ts= sum(nums)
        ls = 0
        ans = []

        for num in nums:
            rs= ts - ls - num
            ans.append(abs(ls- rs))
            ls+= num

        return ans


        