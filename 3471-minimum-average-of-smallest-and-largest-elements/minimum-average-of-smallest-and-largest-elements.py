class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        l=len(nums)//2
        while(l>0):
            mi=min(nums)
            ma=max(nums)
            av=((ma+mi)/2)
            avg.append(av)
            nums.remove(mi)
            nums.remove(ma)
            l-=1
        return min(avg)
        