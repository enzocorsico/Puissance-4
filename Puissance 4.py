from turtle import*
colonnex=[-150,-100,-50,0,50,100,150]
ligney=[-175,-125,-75,-25,25,75]
colonne=0
ligne=0
pion=False
colonne1=[0,0,0,0,0,0]
colonne2=[0,0,0,0,0,0]
colonne3=[0,0,0,0,0,0]
colonne4=[0,0,0,0,0,0]
colonne5=[0,0,0,0,0,0]
colonne6=[0,0,0,0,0,0]
colonne7=[0,0,0,0,0,0]
n=0

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
    global colonne,n,pion,ligne
    colonne=int(input("Colonne: "))
    while colonne<1 or colonne>7:
        colonne=int(input("Veuillez ressaisir une colonne valide: "))
    
    if colonne==1:
        if colonne1[0]+colonne1[1]+colonne1[2]+colonne1[3]+colonne1[4]+colonne1[5]==0:
            colonne1[0]=1
            ligne=1
            pion=True
            return
        
        for d in range(len(colonne1)):
            if colonne1[d]!=0:
                pion=False
            else:
                colonne1[d]=1
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
    


mise_en_place()
Grille_vide()

for w in range(5):
    Coup_possible()
    if pion==True:
        cercle()