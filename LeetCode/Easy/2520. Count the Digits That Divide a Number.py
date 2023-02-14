class Solution:
    def countDigits(self, num: int) -> int:
        # Create a new list and return length of it, where the nums are
        # the odd ones in num
        newlst = [i for i in str(num) if num % int(i) == 0]
        return len(newlst)