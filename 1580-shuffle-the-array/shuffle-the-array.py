class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr=nums[:n]
        arr2=nums[n:]
        arr3=[]
        for i in range(n):
            arr3.append(arr[i])
            arr3.append(arr2[i])
        return arr3
