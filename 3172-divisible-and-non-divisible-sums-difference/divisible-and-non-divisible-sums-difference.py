class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # n1,n2=0,0
        # for i in range(1,n+1):
        #     if(i%m==0):
        #         n1+=i
        #     else:
        #         n2+=i
        # return n2-n1
        total_sum = n * (n + 1) // 2
        k = n // m
        sum2 = m * k * (k + 1) // 2
        return total_sum - 2 * sum2

        