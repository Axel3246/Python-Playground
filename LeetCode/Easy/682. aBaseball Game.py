'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
'''

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        # Basically stack [-1] and stack[-2]. Made it hard 
        last = 0 
        prelast = 0
        for scr in operations:
            # Strip "-" and check if num. Could've just let this at the end and check for op or chars first.
            if scr.lstrip("-").isdigit():
                stack.append(int(scr)) # append
                prelast = stack[len(stack)-2] # #update the var before last
                last = stack[-1]
            else:
                # Append last * 2
                if scr == 'D':
                    stack.append(last*2)
                    prelast = last
                    last = stack[-1]
                # Delete from stack. Update if stack is not empty
                elif scr == 'C':
                    stack.pop()
                    if stack:
                        last = prelast
                        prelast = stack[len(stack)-2]
                # Append last + prelast
                elif scr == '+':
                    stack.append(prelast+last)
                    prelast = last
                    last = stack[-1]
            
        # Return 0 if stack empty, else sum the arr (stack)
        return 0 if not stack else sum(stack)
    
