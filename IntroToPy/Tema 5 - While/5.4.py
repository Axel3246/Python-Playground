a = int(input())
b = int(input())

while a <= b:
    if a%2 == 0:
        print (a)
        a = a + 2
    elif a%2 == 1:
        a = (a+1)
        if a%2 == 0:
            print (a)
            a = a + 1
        else:
            print (a)
            a = a + 1
