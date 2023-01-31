'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving 
whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(" ") # Separamos el string a partir de los espacios
        lista = [word[::-1] for word in split] # Volteamos la palabra por cada palabra en el split
        
        '''
        for word in split:
            lista.append(word[::-1])
        '''
        
        return ' '.join(lista) # los regresamos con los espacios deseados usando join