class Solution:
    def maximum69Number (self, num: int) -> int:
        if('6' not in str(num)):
            return num
        else:
            return int(str(num).replace('6', '9', 1))
