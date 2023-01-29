'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        nlst = s.split()
        if len(nlst) != len(list(pattern)):
            return False
        else:
            mhs = {}
            # TRAVERSE ANY STRING CUZ SAME LENGHT
            for i in range(0, len(pattern), 1):
                print(mhs)
                # IF CHAR NOT IN MAP, ADD IT
                if pattern[i] not in mhs:
                    if nlst[i] not in mhs.values():
                        mhs[pattern[i]] = nlst[i]
                    else:
                        return False
                # IF KEY EXIST CHECK IF THE NEW T[I] IS THE SAME AS THE ONE SAVED
                elif pattern[i] in mhs.keys():
                    if mhs[pattern[i]] != nlst[i]:
                        return False
        return True