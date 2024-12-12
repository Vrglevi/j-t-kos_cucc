import random
def menu():
    while True:
        print("1 gondolkod")
        print("2 géptalálgat")
        print("3 kő papír olló")
        print("4 quiz")


        valasz=int(input("Válassz játékot:"))
        if valasz == 1:
            gondolkod()
            
        elif valasz == 2:
            geptalalgat() 

        elif valasz == 3:
            kopapirollo()
        
        elif valasz == 4:
            quiz()

        else:
            print("Nem játék")

def beker():
    ismeteld= True
    while ismeteld:
        be = input("Kérek egy egész számot 1-100-ig: ")
        if (be.isnumeric()):
            szam=int(be)
            ismeteld=False
        else:
            print("Nem jó formátum")

    return szam

def gondolkod():
    gondolt=random.randint(1,100)
    ja=True
    proba=0
    while ja:
        proba=proba+1
        print (str(proba)+". próba")
        tipp=beker()
        if tipp == gondolt:
            print("Talált "+str(proba)+" lépésből")
            if proba>7:
                print("Béna vagy")
            ja=False  
        elif tipp < gondolt:
            print("A szám kicsi")
        else:
            print("A szám nagy")
    xd = input("Szeretnél még játszani? y/n ")
    while True:
        if xd == "y":
            gondolkod()
        elif xd == "n":
            print("Viszlát")
            menu()
        else:
            print("Nem opció")
    
def kopapirollo():
    igaz=True
    cuccok=["olló","papir","kő"]
    proba=1
    while igaz:
        gep=random.choice(cuccok)
        print(str(proba) + ". Próba")
        valasz=input("Válasz egy cuccot kő, papir, olló : ")
        if valasz in  cuccok:
            if valasz == gep:
                print("Döntetlen")
                proba+=1
            elif valasz == "olló" and gep == "papir":
                print("Nyertél")
                igaz=False
            elif valasz == "papir" and gep == "kő":
                print ("Nyertél")
                igaz=False
            elif valasz == "kő" and gep == "olló":
                print ("Nyertél")
                igaz=False
            else:
                print ("Nem nyert próbálkozz újra")
                proba+=1
        else:
            print("Nem jó cucc")
        
    print("Gratulálok")
    print(str(proba) + " Próbából sikerűlt legyőzni a gépet." )
    bemenet=input("Szeretnél játszani y/n: ")
    if bemenet == "n":
        print ("Viszlát")
        menu()
    elif bemenet == "y":
        kopapirollo()
    else:
        print("Nem opció")

def talalt():
    print("Nagyon örülök!")

def sok():
    global tipp
    global veg
    global kezd
    v = tipp
    #tipp = int(tipp / 2)
    tipp =  int((veg-tipp)/2)+kezd
    veg = v
    if v == tipp:
        print("Csaltál")

def keves():
    global tipp
    global veg
    global kezd
    kezd = tipp
    tipp = int(( veg-tipp)/2) + kezd
    if kezd == tipp:
        print("Csaltál")

def geptalalgat():
    kezd = 1
    veg = 100
    ismet = True
    tipp=int((veg - kezd)  / 2) + kezd

    while ismet:
        print("A tippem "+str(tipp))
        print("Kérem a válaszod!\n1. sok\n2. kevés\n3. talált ")
        valasz = input("1 vagy 2 vagy 3 :")
        
        if valasz == "1":
            sok()
        elif valasz == "2":
            keves()
        elif valasz == "3":
            talalt()
            ismet = False
        else:
            print("\n\nHibás válasz\n\n")
    bemenet=input("Szeretnél játszani y/n: ")
    if bemenet == "n":
        print ("Viszlát")
        menu()
    elif bemenet == "y":
        geptalalgat()
    else:
        print("Nem opció")

def kerdes1():
    global pontok
    print ("Melyik bolygón élünk?")
    print("A. Föld")
    print("B. Szaturnusz")
    print("C. Jupiter")
    print("D. Nap")
    valasz=input("(A/B/C/D):")
    if valasz.upper() == "A":
        print("Helyes válasz +1 pont")
        pontok+=1
    else:
        print("Rossz válasz")

def kerdes2():
    global pontok
    print ("Melyik ember a leggazdagabb?")
    print("A. Elon Musk")
    print("B. Jeff Bezos")
    print("C. Bill Gates")
    print("D. Botika")
    valasz=input("(A/B/C/D):")
    if valasz.upper() == "D":
        print("Helyes válasz +1 pont")
        pontok+=1
    else:
        print("Rossz válasz")

def kerdes3():
    global pontok
    print ("Milyen pénz nemet használ Japán?")
    print("A. Forint")
    print("B. Dollár")
    print("C. Peso")
    print("D. Yen")
    valasz=input("(A/B/C/D):")
    if valasz.upper() == "D":
        print("Helyes válasz +1 pont")
        pontok+=1
    else:
        print("Rossz válasz")
def kerdes4():
    global pontok
    print ("Melyik a készitő két kedvenc állata?")
    print("A. Kapibara")
    print("B. Zsiráf")
    print("C. Fóka")
    print("D. Madárpók")
    valasz=input("1.(A/B/C/D):")
    valasz2=input("2.(A/B/C/D):")
    if valasz.upper() == "A" and valasz2.upper() == "C" or valasz.upper() == "C" and valasz2.upper() == "A":
        print("Helyes válasz +1 pont")
        pontok+=1
    else:
        print("Rossz válasz")


def quiz():
    global pontok
    pontok=0
    cica=[kerdes1, kerdes2, kerdes3, kerdes4]
    
    for i in range (4):
        random_cica=random.choice(cica)
        random_cica()
        cica.remove(random_cica)
    print (str(pontok) + "pontot értél el")
    

    bemenet=input("Szeretnél játszani y/n: ")
    if bemenet == "n":
        print ("Viszlát")
        menu()
    elif bemenet == "y":
        quiz()
    else:
        print("Nem opció")

menu()