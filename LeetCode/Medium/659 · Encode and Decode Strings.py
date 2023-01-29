
strs = ["lint", "code", "loves", "you"]

def encode(strs):
    enc = ""
    for r in strs:
        enc += str(len(r)) + '#' + r
    #print(enc)
    return enc

def decode(strs):
    res = [] # i = input string, res = arr
    i = 0
    # while i hasn't finished traversing the array
    while i < len(strs):
        j = i
        # Check delimeter position
        while strs[j] != "#":
            j += 1
        # get real lenght of arr by getting the integer we encoded
        lenght = int(strs[i:j])
        # append from the first letter (next to #) to the final one
        res.append(strs[j+1 : j +1 +lenght])
        # next string (end of first word)
        i = j + 1 + lenght
    
    return res

a = encode(strs)
b = decode(a)
print(a)
print(b)


