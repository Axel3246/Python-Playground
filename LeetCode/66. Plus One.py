class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # MAP AND JOIN ALL INTEGERS TO STRING
        a = int(''.join(map(str,digits)))
        # SUM ONE
        a += 1
        # USE EVAL TO CREATE NEW LIST WITH THE CHARACTERS AS INT
        b = [eval(num) for num in str(a)]
        return b

'''
similar solution, but i guess its less time consuming because it doesn't use list comprehension to eval every char

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        number += 1
        return map(int,str(number))
'''