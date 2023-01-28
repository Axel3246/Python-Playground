'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Hash map
        mapp = {}
        # Count
        for i in sentence:
            mapp[i] = 1 + mapp.get(i,0)
        #print(mapp)
        #print(len(mapp))
        # If len is shorter than the num of chars in alphabet, return false
        return False if len(mapp) < 26 else True
        