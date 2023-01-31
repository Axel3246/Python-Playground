'''
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.

Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".
'''

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Variables
        hmap = {}
        nxt = 0
        res = ""
        # Traverse key for cipher
        for c in key:
            if c not in hmap.keys() and c != " ":
                # chr(ord("a") + nxt) is the next char of the alphabet a-z
                hmap[c] = chr(ord("a") + nxt)
                nxt += 1
        # Decode message
        for c in message:
            if c == " ":
                res += " "
            else:
                res += hmap[c]

        return res