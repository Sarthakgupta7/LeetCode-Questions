class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m=-1
        k=0
        for  i in range(len(arr)):
            if(arr[i]>m):
                m=arr[i]
                k=i
        
        return k
        