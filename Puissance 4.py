from turtle import*
colonne=[-150,-100,-50,0,50,100,150]
ligne=[-175,-125,-75,-25,25,75]

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

def cercle():
    up()
    goto(colonne[x],ligne[y])
    if 
        

Grille_vide()