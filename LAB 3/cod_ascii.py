import math
def toBinary(a):
    l, m=[], []
    for i in a:
        l.append(int(bin(ord(i))[2:]))
    return l

text_tastatura=input("Introdu propozitia: ")
print (toBinary(text_tastatura))