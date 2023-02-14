'''
You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
'''

class Solution:
    def interpret(self, command: str) -> str:

        command = command.replace("()", "o")
        command = command.replace('(al)', 'al')

        return command 


'''
Long Solution
class Solution:
    def interpret(self, command: str) -> str:

        out = ""
        i = 0
   
        while (i < len(command)):
            #print(f'Letter is {command[i]} and i is {i}')
            if command[i] == "(":
                #print(f'Letter + 1 is {command[i+1]}')
                if command[i+1] == "a":
                    out += "al"
                    i += 4
                else:
                    out += "o"
                    i += 2
            else:
                out += "G"
                i += 1

            #print(f'Out is {out}')
        return out

'''