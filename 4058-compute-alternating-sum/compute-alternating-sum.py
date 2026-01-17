# class Solution:
#     def alternatingSum(self, nums: List[int]) -> int:
#         s=0
#         for i in range(len(nums)):
#             if i%2==0:
#                 s+=nums[i]
#             else:
#                 s-=nums[i]
#         return s
class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        return sum(nums[i] if i % 2 == 0 else -nums[i] for i in range(len(nums)))