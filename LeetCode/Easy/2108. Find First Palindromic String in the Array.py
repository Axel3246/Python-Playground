class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            if(word == word[::-1]): # si la palabra es la misma que la reversa
                return word
        return ""