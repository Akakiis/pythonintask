import random
print ("you have to guess the word that will be given by this programm. PRESS ENTER TO BEGIN. WRITE HELP TO MISS THE WORD. WRITE EXIT TO STRUGGLE")
input()
TRUST = 0
score = 0
while TRUST == 0:
    TRUST = 0
    word=random.choice(["Tear","Great","Freeze","Home","Job","Create","Whore","Fire","More"])
    if len(word)==6:
        A=word[0]
        B=word[1]
        C=word[2]
        D=word[3]
        E=word[4]
        P=word[5]
        G=random.sample([A,B,C,D,E,P], 6)
        H=G[1]
        K=G[2]
        N=G[3]
        M=G[4]
        L=G[0]
        Z=G[5]
        V=H+K+N+M+L+Z
        print(V)
    elif len(word)==5:
        A=word[0]
        B=word[1]
        C=word[2]
        D=word[3]
        E=word[4]
        G=random.sample([A,B,C,D,E], 5)
        H=G[1]
        K=G[2]
        N=G[3]
        M=G[4]
        L=G[0]
        V=H+K+N+M+L
        print(V)
    elif len(word)==4:
        A=word[0]
        B=word[1]
        C=word[2]
        D=word[3]
        G=random.sample([A,B,C,D], 4)
        H=G[1]
        K=G[2]
        N=G[3]
        L=G[0]
        V=H+K+N+L
        print(V)
    elif len(word)==3:
        A=word[0]
        B=word[1]
        C=word[2]
        G=random.sample([A,B,C], 3)
        H=G[1]
        K=G[2]
        L=G[0]
        V=H+K+L
        print(V)
    elif len(word)==2:
        A=word[0]
        B=word[1]
        G=random.sample([A,B], 2)
        H=G[1]
        L=G[0]
        V=H+L
        print(V)
      
    x=input()
    if x == word:
        score = score + 5
        print("Right, your score is",score)
    elif x == "exit":
        TRUST = 1
        print("exiting the programm")
    elif x == "help":
        score = score -1
        print("Your word was", word, "you have lost 1 point. Your score is ", score)
    elif x != word:
        score = score - 3
        print("You are wrong, you have lost 3 points. Your score is",score)
    if score <= 0:
        print("You lose")
        break

        
        
