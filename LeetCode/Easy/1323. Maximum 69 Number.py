class Solution:
    def maximum69Number (self, num: int) -> int:
        # BASICALLY FIND THE FIRST OCCURENCE OF 6
        b = str(num)
        b = b.replace("6", "9", 1)
        print(f'b es {b}')
        return int(b)
                
                