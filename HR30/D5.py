"""
Task
Given an integer, n , 
print its first  10 multiples. Each multiple  (where 1<= i <= 10) 
should be printed on a new line in the form: n x i = result.
"""
#Given an integer, , print its first 10  multiples. 

n = int(input())


for i in range (1,11):
    valor = i * n
    print(str(n) + ' x ' + str(i) + ' = ' + str(valor))