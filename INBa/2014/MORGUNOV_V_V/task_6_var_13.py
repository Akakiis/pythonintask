import random
print("Ugadayte odin is sputnikov marsa, type end to finish")
k=0
while k == 0:
    a = ("Fobos", "Deymos")
    c = random.choice(a)
    
    b = input()
    
    if c == b:
        print("YES")
    else:
        print("NO, ty again")
    if b == "end":
        k = k +1