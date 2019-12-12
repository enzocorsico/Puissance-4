from turtle import*


def Grille_vide():
    grille_x=-175
    grille_y=-175
    up()
    color("black")
    for a in range(8):
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
        forward(350)
        grille_x=grille_x+50
        up()
        
        

Grille_vide()