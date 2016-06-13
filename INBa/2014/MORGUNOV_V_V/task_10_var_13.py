print("Your hero has four measures. Power, Intelligence, Stamina, Agility. Also you have 40 points. ")

Pool = 40
endit = 0
P=0
I=0
S=0
A=0
while Pool > 0:
    print("Choose the number")
    print("1 - Power")
    print("2 - Inteilligience")
    print ("3 - Agility")
    print ("4 - stamina")
    print ("5 - retry")
    X=int(input())
    if X == 1:
        print("Type the score you want to increase.")
        z=int(input())
        if z > Pool:
            print("Your number is bigger than pool")
            break
        Pool = Pool - z
        P=P+z
        print("Power - ", P)
        print("Stamina - ", S)
        print("Inteilligience - ", I)
        print("Agility - ", A)
        print ("left points - ", Pool)
    if X == 2:
        print("Type the score you want to increase.")
        z=int(input())
        if z > Pool:
            print("Your number is bigger than pool")
            break
        Pool = Pool - z
        I=I+z
        print("Power - ", P)
        print("Stamina - ", S)
        print("Inteilligience - ", I)
        print("Agility - ", A)
        print ("left points - ", Pool)
    if X == 3:
        print("Type the score you want to increase.")
        z=int(input())
        if z > Pool:
            print("Your number is bigger than pool")
            break
        Pool = Pool - z
        A=A+z
        print("Power - ", P)
        print("Stamina - ", S)
        print("Inteilligience - ", I)
        print("Agility - ", A)
        print ("left points - ", Pool)
    if X == 4:
        print("Type the score you want to increase.")
        z=int(input())
        if z > Pool:
            print("Your number is bigger than pool")
            break
        Pool = Pool - z
        S=S+z
        print("Power - ", P)
        print("Stamina - ", S)
        print("Inteilligience - ", I)
        print("Agility - ", A)
        print ("left points - ", Pool)
    if X == 5:
        print("Select, which one you want to decrease")
        print("1 - Power")
        print("2 - Inteilligience")
        print ("3 - Agility")
        print ("4 - stamina")
        H=int(input())
        print("Type the score, you want to decrease.")
        z=int(input())
        if H == 1:
            if z > P:
                print("Your number is bigger then Power")
                break
            P=P-z
            Pool=Pool+z
            print("Power - ", P)
            print("Stamina - ", S)
            print("Inteilligience - ", I)
            print("Agility - ", A)
            print ("left points - ", Pool)
        elif H == 2:
            if z > I:
                print("Your number is bigger then Intelligience")
                break
            I=I-z
            Pool=Pool+z
            print("Power - ", P)
            print("Stamina - ", S)
            print("Inteilligience - ", I)
            print("Agility - ", A)
            print ("left points - ", Pool)
        elif H == 3:
            if z > A:
                print("Your number is bigger then Agility")
                break
            A=A-z
            Pool=Pool+z
            print("Power - ", P)
            print("Stamina - ", S)
            print("Inteilligience - ", I)
            print("Agility - ", A)
            print ("left points - ", Pool)
        elif H == 4:
            if z > S:
                print ("Your number is bigger then stamina")
                break
            S=S-z
            Pool=Pool+z
            print("Power - ", P)
            print("Stamina - ", S)
            print("Inteilligience - ", I)
            print("Agility - ", A)
            print ("left points - ", Pool)
        