import random
print ("you have to guess the word that will be given by this programm. PRESS ENTER TO BEGIN.")
input()

word=random.choice(["great","freeze","home","job","create","whore","fire","more"])
a=len(word)
print("Lenght of your word is - ",a)

Z=5
if a ==6:
    B=word[0]
    C=word[1]
    D=word[2]
    E=word[3]
    T=word[4]
    Y=word[5]
    print("You have 5 tries to guess letters from the hidden word.")
    while Z > 0:
        G=input()
        if G == B:
            print("yes")
            Z=Z-1
        elif G == C:
            print("yes")
            Z=Z-1
        elif G == D:
            print("yes")
            Z=Z-1
        elif G == E:
            print ("yes")
            Z=Z-1
        elif G ==T:
            print("yes")
            Z=Z-1
        elif G == Y:
            print ("yes")
            Z=Z-1
        elif G!=[B,C,D,E,T,Y]:
            print("no")
            Z=Z-1
    
elif a == 5:
    B=word[0]
    C=word[1]
    D=word[2]
    E=word[3]
    T=word[4]
    print("You have 5 tries to guess letters from the hidden word.")
    while Z > 0:
        G=input()
        if G == B:
            print("yes")
            Z=Z-1
        elif G == C:
            print("yes")
            Z=Z-1
        elif G == D:
            print("yes")
            Z=Z-1
        elif G == E:
            print ("yes")
            Z=Z-1
        elif G == T:
            print ("yes")
            Z=Z-1
        elif G!=[B,C,D,E,T]:
            print("no")
            Z=Z-1
elif a == 4:
    B=word[0]
    C=word[1]
    D=word[2]
    E=word[3]
    print("You have 5 tries to guess letters from the hidden word.")
    while Z > 0:
        G=input()
        if G == B:
            print("yes")
            Z=Z-1
        elif G == C:
            print("yes")
            Z=Z-1
        elif G == D:
            print("yes")
            Z=Z-1
        elif G == E:
            print("yes")
            Z=Z-1
        elif G!=[B,C,D,E]:
            print("no")
            Z=Z-1
    
elif a == 3:
    B=word[0]
    C=word[1]
    D=word[2]
    Z=5
    print("You have 5 tries to guess letters from the hidden word.")
    while Z > 0:
        G=input()
        if G == B:
            print("yes")
            Z=Z-1
        elif G == C:
            print("yes")
            Z=Z-1
        elif G == D:
            print("yes")
            Z=Z-1
        elif G!=[B,C,D]:
            print("no")
            Z=Z-1
print("You have 1 try to guess the word with the help of recentely guessed letters.")
L=input()
if L == word:
    print("!!!Congritulations!!!")
elif L != word:
    print("you have lost")