import turtle as trt
colonnex=[-150,-100,-50,0,50,100,150]
ligney=[-150,-100,-50,0,50,100]
chiffre=-155
chiffre2=["1","2","3","4","5","6","7"]
colonne=""
ligne=0
joueur=[0,1,2] #Le 0 ne correspond à aucun joueur
couleur=["red","blue"]
pion=False
colonne1=[0,0,0,0,0,0]
colonne2=[0,0,0,0,0,0]
colonne3=[0,0,0,0,0,0]
colonne4=[0,0,0,0,0,0]
colonne5=[0,0,0,0,0,0]
colonne6=[0,0,0,0,0,0]
colonne7=[0,0,0,0,0,0]
n=1
gagnant=0
horizontale=False
verticale=False
diagonale=False

def mise_en_place():
    global chiffre,chiffre2
    trt.up()
    trt.setup(450,450)
    trt.title("Puissance 4")
    trt.speed(26)
    trt.getscreen()
    trt.ht()
    for j in range(7):
        trt.goto(chiffre,150)
        trt.write(chiffre2[j],font=("Arial",15,"normal"))
        chiffre=chiffre+50
    joueur[0]

def Grille_vide():
    trt.tracer(False)
    grille_x=-175
    grille_y=-148
    trt.up()
    trt.color("black")
    for a in range(7):
        trt.up()
        trt.goto(grille_x,grille_y)
        trt.down()
        trt.forward(350)
        grille_y=grille_y+50
        trt.up()
    trt.right(90)
    grille_y=grille_y-50
    for b in range(8):
        trt.up()
        trt.goto(grille_x,grille_y)
        trt.down()
        trt.forward(300)
        grille_x=grille_x+50
        trt.up()
    trt.left(90)

def Coup_possible():
    global colonne,n,pion,ligne,partie
    colonne=trt.textinput("Joueur "+str(joueur[n]),"Saisissez une colonne")
    if colonne=="exit":
        return
        
    while len(colonne)<1 or len(colonne)>1 or len(colonne)==0 or ord(colonne)<49 or ord(colonne)>55:
        colonne=trt.textinput("Joueur "+str(joueur[n]),"Saisissez une colonne valide")
            
    if int(colonne)==1:
        if colonne1[0]!=0 and colonne1[1]!=0 and colonne1[2]!=0 and colonne1[3]!=0 and colonne1[4]!=0 and colonne1[5]!=0:
            pion=False
            if colonne=="exit":
                return
        for d in range(len(colonne1)):
            if colonne1[d]!=0:
                pion=False
            else:
                colonne1[d]=joueur[n]
                ligne=d+1
                pion=True
                return
    
    if int(colonne)==2:
        if colonne2[0]!=0 and colonne2[1]!=0 and colonne2[2]!=0 and colonne2[3]!=0 and colonne2[4]!=0 and colonne2[5]!=0:
            pion=False
            if colonne=="exit":
                return
        for d in range(len(colonne2)):
            if colonne2[d]!=0:
                pion=False
            else:
                colonne2[d]=joueur[n]
                ligne=d+1
                pion=True
                return
    
    if int(colonne)==3:
        if colonne3[0]!=0 and colonne3[1]!=0 and colonne3[2]!=0 and colonne3[3]!=0 and colonne3[4]!=0 and colonne3[5]!=0:
            pion=False
            if colonne=="exit":
                return
        for d in range(len(colonne3)):
            if colonne3[d]!=0:
                pion=False
            else:
                colonne3[d]=joueur[n]
                ligne=d+1
                pion=True
                return
            
    if int(colonne)==4:
        if colonne4[0]!=0 and colonne4[1]!=0 and colonne4[2]!=0 and colonne4[3]!=0 and colonne4[4]!=0 and colonne4[5]!=0:
            pion=False
            if colonne=="exit":
                return
        for d in range(len(colonne4)):
            if colonne4[d]!=0:
                pion=False
            else:
                colonne4[d]=joueur[n]
                ligne=d+1
                pion=True
                return
    
    if int(colonne)==5:
        if colonne5[0]!=0 and colonne5[1]!=0 and colonne5[2]!=0 and colonne5[3]!=0 and colonne5[4]!=0 and colonne5[5]!=0:
            pion=False
            if colonne=="exit":
                return
        for d in range(len(colonne5)):
            if colonne5[d]!=0:
                pion=False
            else:
                colonne5[d]=joueur[n]
                ligne=d+1
                pion=True
                return
    
    if int(colonne)==6:
        if colonne6[0]!=0 and colonne6[1]!=0 and colonne6[2]!=0 and colonne6[3]!=0 and colonne6[4]!=0 and colonne6[5]!=0:
            pion=False
            if colonne=="exit":
                return
        for d in range(len(colonne6)):
            if colonne6[d]!=0:
                pion=False
            else:
                colonne6[d]=joueur[n]
                ligne=d+1
                pion=True
                return
            
    if int(colonne)==7:
        if colonne7[0]!=0 and colonne7[1]!=0 and colonne7[2]!=0 and colonne7[3]!=0 and colonne7[4]!=0 and colonne7[5]!=0:
            pion=False
            if colonne=="exit":
                return
        for d in range(len(colonne7)):
            if colonne7[d]!=0:
                pion=False
            else:
                colonne7[d]=joueur[n]
                ligne=d+1
                pion=True
                return

def cercle():
    global colonne,n
    if colonne=="exit":
        return
    trt.up()
    trt.color(couleur[n-1])
    while ord(colonne)<49 or ord(colonne)>55:
        colonne=trt.textinput("Joueur "+str(joueur[n]),"Saisissez une colonne valide")
    trt.goto(colonnex[int(colonne)-1],ligney[ligne-1])
    trt.down()
    trt.begin_fill()
    trt.circle(25,360)
    trt.end_fill()
    trt.up()

def tour():
    global n
    if n==1:
        n=2
        return
    if n==2:
        n=1
        return

def partie():
    compteur=0
    while Gagne()!=True:
        if colonne=="exit":
            print("")
            trt.goto(-140,200)
            trt.write("Vous avez mis fin à la partie !",font=("Arial",15,"normal"))
            return 
        print("C'est au tour du joueur",joueur[n],"de jouer !")
        Coup_possible()
        if pion==True:
            tour()
            cercle()
            Gagne()
        compteur=compteur+1
    print("")
    trt.goto(-210,200)
    trt.write("La partie est terminée, c'est le joueur "+str(gagnant)+" qui gagne la partie !",font=("Arial",13,"normal"))
    if tour==42:
        trt.goto(-100,200)
        trt.write("La partie est terminée",font=("Arial",15,"normal"))
    
def Horiz():
    global horizontale,gagnant
    if colonne1[0]*colonne2[0]*colonne3[0]*colonne4[0]==1 or colonne2[0]*colonne3[0]*colonne4[0]*colonne5[0]==1 or colonne3[0]*colonne4[0]*colonne5[0]*colonne6[0]==1 or colonne4[0]*colonne5[0]*colonne6[0]*colonne7[0]==1 or colonne1[1]*colonne2[1]*colonne3[1]*colonne4[1]==1 or colonne2[1]*colonne3[1]*colonne4[1]*colonne5[1]==1 or colonne3[1]*colonne4[1]*colonne5[1]*colonne6[1]==1 or colonne4[1]*colonne5[1]*colonne6[1]*colonne7[1]==1 or colonne1[2]*colonne2[2]*colonne3[2]*colonne4[2]==1 or colonne2[2]*colonne3[2]*colonne4[2]*colonne5[2]==1 or colonne3[2]*colonne4[2]*colonne5[2]*colonne6[2]==1 or colonne4[2]*colonne5[2]*colonne6[2]*colonne7[2]==1 or colonne1[3]*colonne2[3]*colonne3[3]*colonne4[3]==1 or colonne2[3]*colonne3[3]*colonne4[3]*colonne5[3]==1 or colonne3[3]*colonne4[3]*colonne5[3]*colonne6[3]==1 or colonne4[3]*colonne5[3]*colonne6[3]*colonne7[3]==1:
        gagnant=1
        horizontale=True
        return True
    elif colonne1[0]*colonne2[0]*colonne3[0]*colonne4[0]==16 or colonne2[0]*colonne3[0]*colonne4[0]*colonne5[0]==16 or colonne3[0]*colonne4[0]*colonne5[0]*colonne6[0]==16 or colonne4[0]*colonne5[0]*colonne6[0]*colonne7[0]==16 or colonne1[1]*colonne2[1]*colonne3[1]*colonne4[1]==16 or colonne2[1]*colonne3[1]*colonne4[1]*colonne5[1]==16 or colonne3[1]*colonne4[1]*colonne5[1]*colonne6[1]==16 or colonne4[1]*colonne5[1]*colonne6[1]*colonne7[1]==16 or colonne1[2]*colonne2[2]*colonne3[2]*colonne4[2]==16 or colonne2[2]*colonne3[2]*colonne4[2]*colonne5[2]==16 or colonne3[2]*colonne4[2]*colonne5[2]*colonne6[2]==16 or colonne4[2]*colonne5[2]*colonne6[2]*colonne7[2]==16 or colonne1[3]*colonne2[3]*colonne3[3]*colonne4[3]==16 or colonne2[3]*colonne3[3]*colonne4[3]*colonne5[3]==16 or colonne3[3]*colonne4[3]*colonne5[3]*colonne6[3]==16 or colonne4[3]*colonne5[3]*colonne6[3]*colonne7[3]==16:
        gagnant=2
        horizontale=True
        return True
    elif colonne1[4]*colonne2[4]*colonne3[4]*colonne4[4]==1 or colonne2[4]*colonne3[4]*colonne4[4]*colonne5[4]==1 or colonne3[4]*colonne4[4]*colonne5[4]*colonne6[4]==1 or colonne4[4]*colonne5[4]*colonne6[4]*colonne7[4]==1 or colonne1[5]*colonne2[5]*colonne3[5]*colonne4[5]==1 or colonne2[5]*colonne3[5]*colonne4[5]*colonne5[5]==1 or colonne3[5]*colonne4[5]*colonne5[5]*colonne6[5]==1 or colonne4[5]*colonne5[5]*colonne6[5]*colonne7[5]==1:
        gagnant=1
        horizontale=True
        return True
    elif colonne1[4]*colonne2[4]*colonne3[4]*colonne4[4]==16 or colonne2[4]*colonne3[4]*colonne4[4]*colonne5[4]==16 or colonne3[4]*colonne4[4]*colonne5[4]*colonne6[4]==16 or colonne4[4]*colonne5[4]*colonne6[4]*colonne7[4]==16 or colonne1[5]*colonne2[5]*colonne3[5]*colonne4[5]==16 or colonne2[5]*colonne3[5]*colonne4[5]*colonne5[5]==16 or colonne3[5]*colonne4[5]*colonne5[5]*colonne6[5]==16 or colonne4[5]*colonne5[5]*colonne6[5]*colonne7[5]==16:
        gagnant=2
        horizontale=True
        return True

def Verti():
    global verticale,gagnant
    if colonne1[0]*colonne1[1]*colonne1[2]*colonne1[3]==1 or colonne1[1]*colonne1[2]*colonne1[3]*colonne1[4]==1 or colonne1[2]*colonne1[3]*colonne1[4]*colonne1[5]==1 or colonne2[0]*colonne2[1]*colonne2[2]*colonne2[3]==1 or colonne2[1]*colonne2[2]*colonne2[3]*colonne2[4]==1 or colonne2[2]*colonne2[3]*colonne2[4]*colonne2[5]==1 or colonne3[0]*colonne3[1]*colonne3[2]*colonne3[3]==1 or colonne3[1]*colonne3[2]*colonne3[3]*colonne3[4]==1 or colonne3[2]*colonne3[3]*colonne3[4]*colonne3[5]==1:
        gagnant=1
        verticale=True
        return True
    elif colonne1[0]*colonne1[1]*colonne1[2]*colonne1[3]==16 or colonne1[1]*colonne1[2]*colonne1[3]*colonne1[4]==16 or colonne1[2]*colonne1[3]*colonne1[4]*colonne1[5]==16 or colonne2[0]*colonne2[1]*colonne2[2]*colonne2[3]==16 or colonne2[1]*colonne2[2]*colonne2[3]*colonne2[4]==16 or colonne2[2]*colonne2[3]*colonne2[4]*colonne2[5]==16 or colonne3[0]*colonne3[1]*colonne3[2]*colonne3[3]==16 or colonne3[1]*colonne3[2]*colonne3[3]*colonne3[4]==16 or colonne3[2]*colonne3[3]*colonne3[4]*colonne3[5]==16:
        gagnant=2
        verticale=True
        return True
    elif colonne4[0]*colonne4[1]*colonne4[2]*colonne4[3]==1 or colonne4[1]*colonne4[2]*colonne4[3]*colonne4[4]==1 or colonne4[2]*colonne4[3]*colonne4[4]*colonne4[5]==1 or colonne5[0]*colonne5[1]*colonne5[2]*colonne5[3]==1 or colonne5[1]*colonne5[2]*colonne5[3]*colonne5[4]==1 or colonne5[2]*colonne5[3]*colonne5[4]*colonne5[5]==1 or colonne6[0]*colonne6[1]*colonne6[2]*colonne6[3]==1 or colonne6[1]*colonne6[2]*colonne6[3]*colonne6[4]==1 or colonne6[2]*colonne6[3]*colonne6[4]*colonne6[5]==1 or colonne7[0]*colonne7[1]*colonne7[2]*colonne7[3]==1 or colonne7[1]*colonne7[2]*colonne7[3]*colonne7[4]==1 or colonne7[2]*colonne7[3]*colonne7[4]*colonne7[5]==1:
        gagnant=1
        verticale=True
        return True
    elif colonne4[0]*colonne4[1]*colonne4[2]*colonne4[3]==16 or colonne4[1]*colonne4[2]*colonne4[3]*colonne4[4]==16 or colonne4[2]*colonne4[3]*colonne4[4]*colonne4[5]==16 or colonne5[0]*colonne5[1]*colonne5[2]*colonne5[3]==16 or colonne5[1]*colonne5[2]*colonne5[3]*colonne5[4]==16 or colonne5[2]*colonne5[3]*colonne5[4]*colonne5[5]==16 or colonne6[0]*colonne6[1]*colonne6[2]*colonne6[3]==16 or colonne6[1]*colonne6[2]*colonne6[3]*colonne6[4]==16 or colonne6[2]*colonne6[3]*colonne6[4]*colonne6[5]==16 or colonne7[0]*colonne7[1]*colonne7[2]*colonne7[3]==16 or colonne7[1]*colonne7[2]*colonne7[3]*colonne7[4]==16 or colonne7[2]*colonne7[3]*colonne7[4]*colonne7[5]==16:
        gagnant=2
        verticale=True
        return True

def Diago():
    global diagonale,gagnant
    #Diagonales Montantes
    if colonne1[2]*colonne2[3]*colonne3[4]*colonne4[5]==1 or colonne1[1]*colonne2[2]*colonne3[3]*colonne4[4]==1 or colonne2[2]*colonne3[3]*colonne4[4]*colonne5[5]==1 or colonne1[0]*colonne2[1]*colonne3[2]*colonne4[3]==1 or colonne2[1]*colonne3[2]*colonne4[3]*colonne5[4]==1 or colonne3[2]*colonne4[3]*colonne5[4]*colonne6[5]==1 or colonne2[0]*colonne3[1]*colonne4[2]*colonne5[3]==1 or colonne3[1]*colonne4[2]*colonne5[3]*colonne6[4]==1 or colonne4[2]*colonne5[3]*colonne6[4]*colonne7[5]==1 or colonne3[0]*colonne4[1]*colonne5[2]*colonne6[3]==1 or colonne4[1]*colonne5[2]*colonne6[3]*colonne7[4]==1 or colonne4[0]*colonne5[1]*colonne6[2]*colonne7[3]==1:
        gagnant=1
        diagonale=True
        return True
    elif colonne1[2]*colonne2[3]*colonne3[4]*colonne4[5]==16 or colonne1[1]*colonne2[2]*colonne3[3]*colonne4[4]==16 or colonne2[2]*colonne3[3]*colonne4[4]*colonne5[5]==16 or colonne1[0]*colonne2[1]*colonne3[2]*colonne4[3]==16 or colonne2[1]*colonne3[2]*colonne4[3]*colonne5[4]==16 or colonne3[2]*colonne4[3]*colonne5[4]*colonne6[5]==16 or colonne2[0]*colonne3[1]*colonne4[2]*colonne5[3]==16 or colonne3[1]*colonne4[2]*colonne5[3]*colonne6[4]==16 or colonne4[2]*colonne5[3]*colonne6[4]*colonne7[5]==16 or colonne3[0]*colonne4[1]*colonne5[2]*colonne6[3]==16 or colonne4[1]*colonne5[2]*colonne6[3]*colonne7[4]==16 or colonne4[0]*colonne5[1]*colonne6[2]*colonne7[3]==16:
        gagnant=2
        diagonale=True
        return True
    #Diagonales Descendantes
    elif colonne1[3]*colonne2[2]*colonne3[1]*colonne4[0]==1 or colonne1[4]*colonne2[3]*colonne3[2]*colonne4[1]==1 or colonne2[3]*colonne3[2]*colonne4[1]*colonne5[0]==1 or colonne1[5]*colonne2[4]*colonne3[3]*colonne4[2]==1 or colonne2[4]*colonne3[3]*colonne4[2]*colonne5[1]==1 or colonne3[3]*colonne4[2]*colonne5[1]*colonne6[0]==1 or colonne2[5]*colonne3[4]*colonne4[3]*colonne5[2]==1 or colonne3[4]*colonne4[3]*colonne5[2]*colonne6[1]==1 or colonne4[3]*colonne5[2]*colonne6[1]*colonne7[0]==1 or colonne3[5]*colonne4[4]*colonne5[3]*colonne6[2]==1 or colonne4[4]*colonne5[3]*colonne6[2]*colonne7[1]==1 or colonne4[5]*colonne5[4]*colonne6[3]*colonne7[2]==1:
        gagnant=1
        diagonale=True
        return True
    elif colonne1[3]*colonne2[2]*colonne3[1]*colonne4[0]==16 or colonne1[4]*colonne2[3]*colonne3[2]*colonne4[1]==16 or colonne2[3]*colonne3[2]*colonne4[1]*colonne5[0]==16 or colonne1[5]*colonne2[4]*colonne3[3]*colonne4[2]==16 or colonne2[4]*colonne3[3]*colonne4[2]*colonne5[1]==16 or colonne3[3]*colonne4[2]*colonne5[1]*colonne6[0]==16 or colonne2[5]*colonne3[4]*colonne4[3]*colonne5[2]==16 or colonne3[4]*colonne4[3]*colonne5[2]*colonne6[1]==16 or colonne4[3]*colonne5[2]*colonne6[1]*colonne7[0]==16 or colonne3[5]*colonne4[4]*colonne5[3]*colonne6[2]==16 or colonne4[4]*colonne5[3]*colonne6[2]*colonne7[1]==16 or colonne4[5]*colonne5[4]*colonne6[3]*colonne7[2]==16:
        gagnant=2
        diagonale=True
        return True

def Gagne():
    if Horiz()==True:
        return True
    if Verti()==True:
        return True
    if Diago()==True:
        return True

mise_en_place()
Grille_vide()
partie()
trt.exitonclick()