class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        e,o=0,0
        for i in range(1,(2*n)+1):
            if(i%2==0):
                e+=i
            else:
                o+=i
        return e-o
        