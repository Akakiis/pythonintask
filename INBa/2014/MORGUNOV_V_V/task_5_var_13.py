import random
random.seed()
z =0
while z == 0:
    print("Programma pokazet vam odnogo is 12 apostolov, type end to exit:")
    a=random.choice(["Andrey", "Petr", "Ioann", "Iakov", "Filipp", "Varfolomey", "Matfey", "Foma", "Iakov", "Faddey", "Simon", "Iuda"])
    print(a)
    if input()=="end":
        z = z + 1