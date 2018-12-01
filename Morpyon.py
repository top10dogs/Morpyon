def partie(case):
    print("    |   |    ")
    print("  " + case[6] + " | " + case[7] + " | " + case[8]  )
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print("  " + case[3] + " | " + case[4] + " | " + case[5] )
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print("  " + case[0] + " | " + case[1] + " | " + case[2]  )
    print("    |   |    ")

def quellecase(choix):
    loop=0
    while loop==0:
        print("Entrer votre case 1-9")
        choix=input()
        if choix.isnumeric()==True:
            choix=int(choix)
            if 1 <= choix <= 9:
                loop=1
    return choix

def quiagagne(c,l):
    return (c[6]==l and c[4]==l and c[2]==l or
           c[6]==l and c[7]==l and c[8]==l or
           c[6]==l and c[3]==l and c[0]==l or
           c[7]==l and c[4]==l and c[1]==l or
           c[8]==l and c[5]==l and c[2]==l or
           c[8]==l and c[4]==l and c[0]==l or
           c[3]==l and c[4]==l and c[5]==l or
           c[0]==l and c[1]==l and c[2]==l)

def egalite(c):
    return (c[0]!=" " and c[1]!=" " and c[2]!=" " and
            c[3]!=" " and c[4]!=" " and c[5]!=" " and
            c[6]!=" " and c[7]!=" " and c[8]!=" ")

joueur=0
case = [" "," "," "," "," "," "," "," "," "]
etat=1
print("Entrer nom du joueur 1")
joueur1=input()
print("Entrer nom du joueur 2")
joueur2=input()
partie(case)
while etat!=0:
    choix=0
    choix = quellecase(choix)
    if case[choix-1]==" " and joueur%2==1: 
        case[choix-1]="0"
        joueur=joueur+1
        partie(case)
    elif case[choix-1]==" " and joueur%2==0:
        case[choix-1]="X"
        joueur=joueur+1
        partie(case)
    if quiagagne(case,"0")==True:
        print(joueur1+" a gagné avec 0")
        etat=0
    elif quiagagne(case,"X")==True:
        print(joueur2+" a gagné avec X")
        etat=0
    elif egalite(case)==True:
        print("Egalité")
        etat=0

      
    
