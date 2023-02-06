def hr (x):
    total = x * 3600
    return total

def minu(y):
    total = y *60
    return total

def seg(z):
    total = z
    return total

def main():
    h = int(input())
    m = int(input())
    s = int(input())
    hora = hr(h)
    minuto = minu(m)
    segundo = seg(s)
    print(hora + minuto + segundo)
    
main()
