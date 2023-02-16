'''
Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

'''

class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        sent = ['' for i in lst]

        for i in lst:
            sent[int(i[-1])-1] = i[:len(i)-1]

        return " ".join(sent)
        