import random
print("Ugadayte odin is sputnikov marsa, type end to finish")
e = 0
g = 0
while g == 0:

    a = ("Fobos", "Deymos")
    c = random.choice(a)
    b = input()
    
    
    if c == b:
        g = 0
        e = e + 100
        print("YES, Vashi ochki" ,e)
          
    elif b == "end":
        break
             
    elif g == 0:
        print("NO, ty again")


