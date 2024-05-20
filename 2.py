import random

list = [3, 4, 5, 8, 12, 13, 15, 17]
choices = random.choices(list, k = 3)
print(a:=choices[0], b:=choices[1], c:=choices[2],)

if a+b > c:
    if a**2 + b**2 == c**2:
        print(True)
    else: print(False)
elif a+c > b:
    if a**2 + c**2 == b**2:
        print(True)
    else: print(False)
else:
    if b**2 + c**2 == a**2:
        print(True)
    else: print(False)