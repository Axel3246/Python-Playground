"""
ask
Given a string, S, of length N that is indexed from 0 to N-1, 
print its even-indexed and odd-indexed characters as 2 space-separated 
strings on a single line.
"""

T = int(input())

for i in range(T):
    stri = str(input())
    print(stri[::2], stri[1::2]) ## :: mueve las letras segun el parametro