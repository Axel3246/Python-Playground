def pies(x):
    totalcm = x * 30.48
    return totalcm

def pulgadas(y):
    totalcm = y * 2.54
    return totalcm

def yardas(z):
    totalcm = z * 91.44
    return totalcm
    
def main():
    opcion = int(input())
    valor = int(input())
    if opcion>=1 and opcion<=3 and valor>0:
        if opcion == 1:
            print (pies(valor))
        elif opcion == 2:
            print (pulgadas(valor))
        else:
            print (yardas(valor))
    else:
        print ("Error")

main()
