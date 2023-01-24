class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1) #juntmamos el string de la lista
        b = ''.join(word2) #juntamos el string de la lista 2
        return a == b
        # equivalente a ''.join(word1) == ''.join(word2)