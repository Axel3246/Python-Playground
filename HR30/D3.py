"""
Task
Given an integer, n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
"""
integer = int(input())

if integer%2 == 1:
    print ("Weird")
elif(integer%2 == 0) and (2<= integer) and (integer<=5):
    print ("Not Weird")
elif(integer%2 == 0) and (6<= integer) and (integer <= 20):
    print ("Weird")
else:
    print ("Not Weird")