import turtle as trt

#Définition des variables
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

def mise_en_place(): #Fonction pour mettre en place la fenêtre turtle
    global chiffre,chiffre2
    trt.up() #Empêche turtle de tracer
    trt.setup(450,450) #Défini la taille de la fenêtre
    trt.title("Puissance 4") #Défini le nom de la fenêtre
    trt.speed(26) #Défini la vitesse de tracé
    trt.getscreen() #Affiche la fenêtre à l'écran
    trt.ht() #Fait disparaitre le curseur de turtle
    for j in range(7): #Boucle pour tracer les chiffres des colonnes
        trt.goto(chiffre,150) #Défini la position de turtle
        trt.write(chiffre2[j],font=("Arial",15,"normal")) #Ecrit le texte  de l'emplacement j de la variable chiffre2
        chiffre=chiffre+50 #Ajoute 50 aux coordonnées x
    joueur[0]

def Grille_vide(): #Fonction pour tracer la grille
    trt.tracer(False) #Enlève le tracer pour plus de vitesse dans le programme
    grille_x=-175
    grille_y=-148
    trt.up()
    trt.color("black") #Change la couleur d'écriture de turtle
    for a in range(7): #Trace les traits horizontaux
        trt.up()
        trt.goto(grille_x,grille_y)
        trt.down() #Baisse la tête de turtle pour tracer
        trt.forward(350) #Avance de 350
        grille_y=grille_y+50
        trt.up() #Lève la tête de turtle pour l'enpêcher de tracer
    trt.right(90) #Tourne de 90° vers la droite
    grille_y=grille_y-50
    for b in range(8): #Trace les traits verticaux
        trt.up()
        trt.goto(grille_x,grille_y)
        trt.down()
        trt.forward(300)
        grille_x=grille_x+50
        trt.up()
    trt.left(90)

def Coup_possible():
    global colonne,n,pion,ligne,partie
    colonne=trt.textinput("Joueur "+str(joueur[n]),"Saisissez une colonne") #Demande une colonne à l'utilisateur
    if colonne=="exit": #Si colonne correspond au mot exit alors le programme s'arrête
        return
        
    while len(colonne)<1 or len(colonne)>1 or len(colonne)==0 or ord(colonne)<49 or ord(colonne)>55: #Boucle tant que pour éviter les erreurs de frappe
        colonne=trt.textinput("Joueur "+str(joueur[n]),"Saisissez une colonne valide") #Redemande un numéro de colonne
            
    if int(colonne)==1:
        if colonne1[0]!=0 and colonne1[1]!=0 and colonne1[2]!=0 and colonne1[3]!=0 and colonne1[4]!=0 and colonne1[5]!=0: #Test pour vérifier s la colonne n'est pas pleine
            pion=False #Si la colonne est pleine, le pion ne se trace pas
            if colonne=="exit":
                return
        for d in range(len(colonne1)): #Boucle pour trouver où tracer le pion (elle parcourt la liste pour trouver un endroit vide de la liste)
            if colonne1[d]!=0: #Si l'élément d de la liste est différent de 0 cela veut dire qu'il y a un pion dans cette ligne et cette colonne
                pion=False
            else:
                colonne1[d]=joueur[n] #Sinon l'élément d de la liste prend le numéro du joueur qui joue actuellement
                ligne=d+1 #Affecte à la variable ligne d+1 pour les calculs qui suivent dans une autre fonction
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
    trt.up() #Lève la tête de turtle pour ne pas qu'elle trace
    trt.color(couleur[n-1]) #Prend la couleur du joueur qui est entrain de jouer
    while ord(colonne)<49 or ord(colonne)>55:
        colonne=trt.textinput("Joueur "+str(joueur[n]),"Saisissez une colonne valide")
    trt.goto(colonnex[int(colonne)-1],ligney[ligne-1]) #Turtle va au coordonnée de la bonne ligne et colonne
    trt.down() #Baisse la tête de turtle pour tracer
    trt.begin_fill() #Commence le remplissage du cercle
    trt.circle(25,360) #Trace un cercle de rayon 25
    trt.end_fill() #Fini le remplissage du cercle
    trt.up() #Lève la tête de turtle pour ne pas tracer

def tour(): #Cette fonction sert à faire les tours, à basculé du joueur 1 au 2 et ainsi de suite
    global n
    if n==1: #Si n est égale à 1
        n=2 #Affecte 2 à la variable n
        return #Stop la fonction
    if n==2: #Si n est égal à 2
        n=1 #Affecte 1 à la variable n
        return #Stop la fonction

def partie():
    compteur=0 #Compteur pour savoir quand 
    while Gagne()!=True: #Tant que la fonction Gagne retourne Vrai
        if colonne=="exit":
            trt.goto(-140,200) #Déplace turtle à la bonne position
            trt.write("Vous avez mis fin à la partie !",font=("Arial",15,"normal")) #Ecrit sur la fenêtre turtle le message
            return 
        Coup_possible() #Fait la fonction Coup_possible
        if pion==True: #Si le bouléen pion est vrai
            tour() #Fait la fonction tour
            cercle() #Fait la fonction cercle
            Gagne() #Fait la fonction Gagne
        compteur=compteur+1 #Ajoute 1 à la variable compteur
    trt.goto(-210,200) #Déplace turtle à la bonne position
    trt.write("La partie est terminée, c'est le joueur "+str(gagnant)+" qui gagne la partie !",font=("Arial",13,"normal")) #Ecrit le message sur la fenêtre turtle
    if compteur==42: #Si compteur est égal à 42
        trt.goto(-100,200) #Déplace turtle à la bonne position
        trt.write("La partie est terminée",font=("Arial",15,"normal")) #Ecrit le message sur la fenêtre turtle

#Les fonctions ci-dessous permettent de savoir quand quelqu'un à gagner, le principe est le même dans les trois fonctions qui suivent.
#Pour savoir quand quelqu'un gagne, on multiplie les bonnes lignes et colonnes nécessaires pour aligner 4 pions,
#Si toutes les bonnes cases pour gagner appartiennent au joueur 1 alors cela fait 1*1*1*1=1 or si il y a un pions du joueur 2 alors le résultat sera 2 ou alors si une case n'appartient a personne alors ça fait 0,
#Si toutes les bonne cases pour gagneer appartiennent au joueur 2 alors cela fait 2*2*2*2=16 or si il y a un pions du joueur 1 alors cela fait 8 ou alors si une case n'appartient a personne alors ça fait 0.
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

def Gagne(): #Définition de la fonction Gagne
    if Horiz()==True: #Si la fonction des victoires horizontale alors le test retourne vrai
        return True
    if Verti()==True: #Si la fonction des victoires verticale alors le test retourne vrai
        return True
    if Diago()==True: #Si la fonction des victoires diagonale alors le test retourne vrai
        return True

#Les fonctions ci-dessous se lancent pour commencer le jeu
mise_en_place()
Grille_vide()
partie()
trt.exitonclick() #Ferme la fenêtre turtle si il y a un clique sur la fenêtre turtle