import re # import regexp

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(s == "" or len(s) == 1): # si len es 1 o "" retorna true
            return True
        else:
            
            news = re.sub('[^a-zA-Z0-9]', '', s) # regexp match
            news = news.upper()
            news = news.lower()
            print(news)
            if(news == news[::-1]): #checamos si coinciden
                #print(f' s: {s}')
                #print(f's-1: {s[::-1]}')
                return True
            return False
        
'''
Mejor solución
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c for c in s.lower() if c.isalnum()] . ##### isalnum() es una funcion de python que regresa solo carácteres alfanuméricos
        return new_s == new_s[::-1]
'''