from turtle import*
colonnex=[-150,-100,-50,0,50,100,150]
ligney=[-175,-125,-75,-25,25,75]
colonne=0
ligne=0
joueur=[0,1,2]
pion=False
colonne1=[0,0,0,0,0,0]
colonne2=[0,0,0,0,0,0]
colonne3=[0,0,0,0,0,0]
colonne4=[0,0,0,0,0,0]
colonne5=[0,0,0,0,0,0]
colonne6=[0,0,0,0,0,0]
colonne7=[0,0,0,0,0,0]
n=1

def mise_en_place():
    getscreen()
    speed(10)
    #ht()
    joueur[0]





def Grille_vide():
    grille_x=-175
    grille_y=-175
    up()
    color("black")
    for a in range(7):
        up()
        goto(grille_x,grille_y)
        down()
        forward(350)
        grille_y=grille_y+50
        up()
    right(90)
    grille_y=grille_y-50
    for b in range(8):
        up()
        goto(grille_x,grille_y)
        down()
        forward(300)
        grille_x=grille_x+50
        up()
    left(90)



def Coup_possible():
    global colonne,n,pion,ligne
    colonne=int(input("Colonne: "))
    while colonne<1 or colonne>7:
        colonne=int(input("Veuillez ressaisir une colonne valide: "))
    
    if colonne==1:
        if colonne1[0]!=0 and colonne1[1]!=0 and colonne1[2]!=0 and colonne1[3]!=0 and colonne1[4]!=0 and colonne1[5]!=0:
            pion=False
            while colonne<1 or colonne>7 or colonne==1:
                colonne=int(input("Veuillez ressaisir une colonne valide: "))
        for d in range(len(colonne1)):
            if colonne1[d]!=0:
                pion=False
            else:
                colonne1[d]=joueur
                ligne=d+1
                pion=True
                return
    
    if colonne==2:
        if colonne2[0]!=0 and colonne2[1]!=0 and colonne2[2]!=0 and colonne2[3]!=0 and colonne2[4]!=0 and colonne2[5]!=0:
            pion=False
            while colonne<1 or colonne>7 or colonne==2:
                colonne=int(input("Veuillez ressaisir une colonne valide: "))
        for d in range(len(colonne2)):
            if colonne2[d]!=0:
                pion=False
            else:
                colonne2[d]=joueur
                ligne=d+1
                pion=True
                return
    
    if colonne==3:
        if colonne3[0]!=0 and colonne3[1]!=0 and colonne3[2]!=0 and colonne3[3]!=0 and colonne3[4]!=0 and colonne3[5]!=0:
            pion=False
            while colonne<1 or colonne>7 or colonne==3:
                colonne=int(input("Veuillez ressaisir une colonne valide: "))
        for d in range(len(colonne3)):
            if colonne3[d]!=0:
                pion=False
            else:
                colonne3[d]=joueur
                ligne=d+1
                pion=True
                return
            
    if colonne==4:
        if colonne4[0]!=0 and colonne4[1]!=0 and colonne4[2]!=0 and colonne4[3]!=0 and colonne4[4]!=0 and colonne4[5]!=0:
            pion=False
            while colonne<1 or colonne>7 or colonne==4:
                colonne=int(input("Veuillez ressaisir une colonne valide: "))
        for d in range(len(colonne4)):
            if colonne4[d]!=0:
                pion=False
            else:
                colonne4[d]=joueur
                ligne=d+1
                pion=True
                return
    
    if colonne==5:
        if colonne5[0]!=0 and colonne5[1]!=0 and colonne5[2]!=0 and colonne5[3]!=0 and colonne5[4]!=0 and colonne5[5]!=0:
            pion=False
            while colonne<1 or colonne>7 or colonne==5:
                colonne=int(input("Veuillez ressaisir une colonne valide: "))
        for d in range(len(colonne5)):
            if colonne5[d]!=0:
                pion=False
            else:
                colonne5[d]=joueur
                ligne=d+1
                pion=True
                return
    
    if colonne==6:
        if colonne6[0]!=0 and colonne6[1]!=0 and colonne6[2]!=0 and colonne6[3]!=0 and colonne6[4]!=0 and colonne6[5]!=0:
            pion=False
            while colonne<1 or colonne>7 or colonne==6:
                colonne=int(input("Veuillez ressaisir une colonne valide: "))
        for d in range(len(colonne6)):
            if colonne6[d]!=0:
                pion=False
            else:
                colonne6[d]=joueur
                ligne=d+1
                pion=True
                return
            
    if colonne==7:
        if colonne7[0]!=0 and colonne7[1]!=0 and colonne7[2]!=0 and colonne7[3]!=0 and colonne7[4]!=0 and colonne7[5]!=0:
            pion=False
            while colonne<1 or colonne>7 or colonne==7:
                colonne=int(input("Veuillez ressaisir une colonne valide: "))
        for d in range(len(colonne7)):
            if colonne7[d]!=0:
                pion=False
            else:
                colonne7[d]=joueur
                ligne=d+1
                pion=True
                return



def cercle():
    up()
    goto(colonnex[colonne-1],ligney[ligne-1])
    down()
    begin_fill()
    circle(25,360)
    end_fill()
    up()

def tour():
    global n
    if n==1:
        n=2
        return
    if n==2:
        n=1
        return


z=100
mise_en_place()
Grille_vide()
print("C'est au tour du joueur",joueur[n],"de jouer !")
for w in range(z):
    Coup_possible()
    if pion==True:
        tour()
        cercle()
        print("C'est au tour du joueur",joueur[n],"de jouer !")        