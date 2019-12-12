from turtle import*
colonne=[-150,-100,-50,0,50,100,150]
ligne=[-175,-125,-75,-25,25,75]
l=0
c=0
colonne1=[0,0,0,0,0,0]
colonne2=[0,0,0,0,0,0]
colonne3=[0,0,0,0,0,0]
colonne4=[0,0,0,0,0,0]
colonne5=[0,0,0,0,0,0]
colonne6=[0,0,0,0,0,0]
colonne7=[0,0,0,0,0,0]

def mise_en_place():
    getscreen()
    speed(10)
    #ht()





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
    global l,c
    l=int(input("Ligne: "))
    c=int(input("Colonne: "))
    while l<1 or l>6:
        l=int(input("Veuillez ressaisir une ligne valide: "))
    while c<1 or c>7:
        c=int(input("Veuillez ressaisir une colonne valide: "))
    if 

def cercle():
    up()
    goto(colonne[c-1],ligne[l-1])
    down()
    begin_fill()
    circle(25,360)
    end_fill()
    up()
    

mise_en_place()
Grille_vide()
Coup_possible()
if Coup_possible==True:
    cercle()