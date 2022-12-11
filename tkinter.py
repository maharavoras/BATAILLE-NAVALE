from tkinter import *
from tkinter.messagebox import showinfo

Fenetre=Tk()
Fenetre.title("Touché,coulé !")

Destoyer=3
Sous_marin=2
Croiseur=1


def init():
    global tour, sous_tour, Flotte_J1, Flotte_J2, Carte_J1, Carte_J2, Placement_Bateaux, Points_J1, Points_J2, Bateaux_Existants, Longueur_Bateaux, Fin, Reconnaissance, Avion_utilise_J1, Avion_utilise_J2, Missile, Missile_utilise_J1, Missile_utilise_J2, Orientation, xBis, yBis
    tour=1
    Bateaux_Existants=["Destroyer", "Sous_marin", "Croiseur"]
    Longueur_Bateaux=[3,2,1]
    Fin="NON"
    Reconnaissance="NON"
    Missile="NON"
    Avion_utilise_J1="NON"
    Avion_utilise_J2="NON"
    Missile_utilise_J1="NON"
    Missile_utilise_J2="NON"
    Orientation="horizontal"
    xBis=-1
    yBis=-1
    Flotte_J1=[[Ecran_J1.create_rectangle(20+i*20 , 20+j*20 , 40+i*20 , 40+j*20, fill="#0040FF",width=1,outline="#000066",tag="Flotte_J1")for i in range(10)]for j in range(5)] # Ã©cran qui montre l'Ã©tat de la flotte du joueur 1
    Flotte_J2=[[Ecran_J2.create_rectangle(20+i*20 , 20+j*20 , 40+i*20 , 40+j*20, fill="#0040FF",width=1,outline="#000066",tag="Flotte_J2")for i in range(10)]for j in range(5)] # Ã©cran qui montre l'Ã©tat de la flotte du joueur 2
    Carte_J1=[[Ecran_J1.create_rectangle(275+i*35 , 275+j*35 , 310+i*35 , 310+j*35, fill="#0040FF",width=1,outline="#000066",tag="Carte_J1")for i in range(10)]for j in range(5)] # Ã©cran de jeu du joueur 1
    Carte_J2=[[Ecran_J2.create_rectangle(275+i*35 , 275+j*35 , 310+i*35 , 310+j*35, fill="#0040FF",width=1,outline="#000066",tag="Carte_J2")for i in range(10)]for j in range(5)] # Ã©cran de jeu du joueur 2
    sous_tour=0
    Points_J1=0
    Points_J2=0
    Placement_Bateaux="OK"
    Ecran_J1.bind("<Button-1>",Jeu)
    Ecran_J1.bind("<Button-2>",Jeu)
    Ecran_J1.bind("<Button-3>",Jeu)
    Ecran_J1.bind("<Motion>",Jeu)
    Ecran_J2.bind("<Button-1>",Jeu)
    Ecran_J2.bind("<Button-2>",Jeu)
    Ecran_J2.bind("<Button-3>",Jeu)
    Ecran_J2.bind("<Motion>",Jeu)
    

def CoordonneesXY(evt,a, Flotte_str, Carte_str ,Ecran):
    if Flotte_str in Ecran.gettags(a):
        x=int((evt.x-20)/20)
        y=int((evt.y-20)/20)
        if x<=11 or y<=11:
            return y,x
        else:
            return y-1,x-1
    elif Carte_str in Ecran.gettags(a):
        x=int((evt.x-275)/35)
        y=int((evt.y-275)/35)
        if x<=11 or y<=11:
            return y,x
        else:
            return y-1,x-1
    else:
        return 0,0
    
def Reconnaissance():
    global Reconnaissance, Missile, Placement_Bateaux, Avion_utilise_J1, Avion_utilise_J2, tour
    xBis=-1
    yBis=-1
    if Placement_Bateaux=="NON" :
        if tour==1 and Avion_utilise_J1=="NON" :
            Reconnaissance="OUI"
            Missile="NON"
            Ecran_J1.bind("<Motion>", Jeu)
        elif tour==2 and Avion_utilise_J2=="NON" :
            Reconnaissance="OUI"
            Missile="NON"
            Ecran_J2.bind("<Motion>", Jeu)
        else:
            showinfo("TouchÃ©, coulÃ© ! Info","Vous avez dÃ©jÃ  utilisÃ© un avion de reconnaissance, vous ne pouvez plus en envoyer.")

def Missile():
    global Missile, Reconnaissance, Placement_Bateaux, Missile_utilise_J1, Missile_utilise_J2, tour
    if Placement_Bateaux=="NON" :
        if tour==1 and Missile_utilise_J1=="NON" :
            Missile="OUI"
            Reconnaissance="NON"
        elif tour==2 and Missile_utilise_J2=="NON" :
            Missile="OUI"
            Reconnaissance="NON"
        else:
            showinfo("TouchÃ©, coulÃ© ! Info","Vous avez dÃ©jÃ  utilisÃ© un missile de croisiÃ¨re, vous ne pouvez plus en envoyer.")
    
def TourSuivant():
    global tour, sous_tour, Placement_Bateaux, Fin, Reconnaissance, Orientation
    if Points_J1==19 :
        Ecran_J2.pack(side=RIGHT)
        showinfo("TouchÃ©, coulÃ© ! Info", "Victoire du joueur 1 !")
    elif Points_J2==19 :
        Ecran_J2.pack_forget() #Pour mettre les 2 Ã©crans dans le bon ordre
        Ecran_J1.pack(side=LEFT)
        Ecran_J2.pack(side=LEFT)
        showinfo("TouchÃ©, coulÃ© ! Info", "Victoire du joueur 2 !")
    else :
        if tour==1:
            if sous_tour<6 and Placement_Bateaux=="OK":
                showinfo("Tour info","Votre tour n\'est pas terminÃ©")
            elif sous_tour==0 and Placement_Bateaux!="OK":
                showinfo("Tour info","Votre tour n\'est pas terminÃ©")
            else :
                tour=2
                sous_tour=0
                Ecran_J1.pack_forget()
                showinfo("Tour suivant","Votre tour est terminÃ©, laissez la place au joueur 2")
                Ecran_J2.pack(side=LEFT)
                Orientation="horizontal"
                Ecran_J1.unbind("<Motion>")
        else:
            if sous_tour<6 and Placement_Bateaux=="OK":
                showinfo("Tour info","Votre tour n\'est pas terminÃ©")
            elif sous_tour==0 and Placement_Bateaux!="OK":
                showinfo("Tour info","Votre tour n\'est pas terminÃ©")
            else:
                tour=1
                sous_tour=0
                Placement_Bateaux="NON"
                Ecran_J2.pack_forget()
                showinfo("Tour suivant","Votre tour est terminÃ©, laissez la place au joueur 1")
                Ecran_J1.pack(side=LEFT)
                Orientation="horizontal"
                Ecran_J2.unbind("<Motion>")
                    
    
def Jeu(evt):
    global sous_tour, Flotte_J1, Flotte_J2, Carte_J1, Carte_J2, tour, Placement_Bateaux, Points_J1, Points_J2, Bateaux_Existants, Longueur_Bateaux, Fin, Reconnaissance, Avion_utilise_J1, Avion_utilise_J2, Missile, Missile_utilise_J1, Missile_utilise_J2, Orientation, xBis, yBis
    if tour==1:
        Flotte=Flotte_J1
        Flotte_str="Flotte_J1"
        Flotte_Ennemie=Flotte_J2
        Carte=Carte_J1
        Carte_str="Carte_J1"
        Ecran=Ecran_J1
        Ecran_Ennemi=Ecran_J2
        Points=Points_J1
    elif tour==2:
        Flotte=Flotte_J2
        Flotte_str="Flotte_J2"
        Flotte_Ennemie=Flotte_J1
        Carte=Carte_J2
        Carte_str="Carte_J2"
        Ecran=Ecran_J2
        Ecran_Ennemi=Ecran_J1
        Points=Points_J2
    if Placement_Bateaux=="OK":
        if evt.num==1:
            Orientation="horizontal"
        elif evt.num==3:
            Orientation="vertical"
        if Orientation=="horizontal" :
            b=0
            c=1
        elif Orientation=="vertical":
            b=1
            c=0
        a=Ecran.find_withtag(CURRENT)
        if Flotte_str in Ecran.gettags(a):
            x,y=CoordonneesXY(evt,a, Flotte_str, Carte_str ,Ecran)
            if x<=11 and y<=11:
                if evt.num==2 : 
                    if sous_tour<6 :
                        Bateau=Bateaux_Existants[sous_tour]
                        Longueur=Longueur_Bateaux[sous_tour]
                        if x+b*Longueur>12 or y+c*Longueur>12:
                            showinfo("Placement du bateau incorrect","Le bateau sort de la grille dans ce cas lÃ , veuillez le replacer correctement.")
                        else :
                            d=[]
                            for k in range(Longueur):
                                d.append(Ecran.itemcget((Flotte[x+b*k][y+c*k]),"fill")) #Regarde si l'espace dÃ©signÃ© est dÃ©jÃ  occupÃ© par un bateau
                            if "grey" in d :
                                showinfo("Placement du bateau incorrect","Le bateau occuperait une case dÃ©jÃ  occuppÃ©e par un autre bateau")
                            else :
                                for j in range(Longueur):
                                    Ecran.itemconfig(Flotte[x+b*j][y+c*j],fill="grey",tag="Bateau")
                                sous_tour+=1
                    else:
                        showinfo("TouchÃ©, CoulÃ© ! Info","Pas plus de 6 bateaux")
                elif sous_tour<6:
                    Bateau=Bateaux_Existants[sous_tour]
                    Longueur=Longueur_Bateaux[sous_tour]
                    if xBis!=x or yBis!=y or evt.num==1 or evt.num==3:#Regarde si il est nÃ©cÃ©ssaire de placer un nouveau spectre de bateau
                        for o in range(12):
                            for v in range(12):
                                if Ecran.itemcget((Flotte[o][v]),"fill")!="grey":
                                    Ecran.itemconfig(Flotte[o][v],fill="#0040FF")
                        if x+b*Longueur>12 or y+c*Longueur>12: #Partie qui place un nouveau spectre de bateau
                            Ecran.itemconfig(Flotte[x][y],fill="red")
                        else :
                            d=[]
                            for k in range(Longueur):
                                d.append(Ecran.itemcget((Flotte[x+b*k][y+c*k]),"fill")) #Regarde si l'espace dÃ©signÃ© est dÃ©jÃ  occupÃ© par un bateau
                            if "grey" in d :
                                if d[0]!="grey":
                                    Ecran.itemconfig(Flotte[x][y],fill="red")
                            else :
                                for j in range(Longueur):
                                    if Ecran.itemcget((Flotte[x+b*k][y+c*k]),"fill")!="grey":
                                        Ecran.itemconfig(Flotte[x+b*j][y+c*j],fill="#DDDDDD")
                        xBis=x
                        yBis=y
    elif Reconnaissance=="NON" and Missile=="NON" and Fin=="NON": #Partie de tir
        a=Ecran.find_withtag(CURRENT)
        if Carte_str in Ecran.gettags(a):
            x,y=CoordonneesXY(evt,a ,Flotte_str, Carte_str, Ecran)
            b=Ecran_Ennemi.find_withtag(Flotte_Ennemie[x][y])
            if sous_tour==0 and Reconnaissance=="NON" and Missile=="NON":
                if "Bateau" in Ecran_Ennemi.gettags(b):
                    if Ecran.itemcget((Carte[x][y]),"fill")=="red" :
                        showinfo("TouchÃ©, CoulÃ© ! Info","Vous avez dÃ©jÃ  tirÃ© sur cette case")
                    else:
                        Ecran.itemconfig(Carte[x][y],fill="red")
                        Ecran_Ennemi.itemconfig(Flotte_Ennemie[x][y],fill="red")
                        if tour==1:
                            Points_J1+=1
                        else :
                            Points_J2+=1
                        if Points_J1==19 or Points_J2==19:
                            Fin="OUI"
                            TourSuivant() 
                else :
                    if Ecran.itemcget((Carte[x][y]),"fill")=="white" :
                        showinfo("TouchÃ©, CoulÃ© ! Info","Vous avez dÃ©jÃ  tirÃ© sur cette case")
                    else :
                        Ecran.itemconfig(Carte[x][y],fill="white")
                        Ecran_Ennemi.itemconfig(Flotte_Ennemie[x][y],fill="white")
                sous_tour+=1 #Mettre 1 Ã  laplace du 0
            else:
                showinfo("TouchÃ©,CoulÃ© ! Info","Vous ne pouvez plus jouer pendant ce tour, cliquez sur \"Tour suivant\"")
    elif Reconnaissance=="OUI" and sous_tour<1 and Fin=="NON": #partie "Avion de reconnaissance"
        a=Ecran.find_withtag(CURRENT)
        if Carte_str in Ecran.gettags(a):
            x,y=CoordonneesXY(evt,a ,Flotte_str, Carte_str, Ecran)
            if evt.num==1:
                Orientation="horizontal"
            elif evt.num==3:
                Orientation="vertical"
            if Orientation=="horizontal" :
                b=0
                c=1
            elif Orientation=="vertical":
                b=1
                c=0
            if evt.num==2:
                for i in range(12):
                    x=x*c+i*b
                    y=y*b+i*c
                    d=Ecran_Ennemi.find_withtag(Flotte_Ennemie[x][y])
                    if "Bateau" in Ecran_Ennemi.gettags(d):
                        if Ecran.itemcget((Carte[x][y]),"fill")!="red" :
                            Ecran.itemconfig(Carte[x][y],fill="grey")
                    else :
                        if Ecran.itemcget((Carte[x][y]),"fill")=="#0040FF" or Ecran.itemcget((Carte[x][y]),"fill")=="#DDDDDD":
                            Ecran.itemconfig(Carte[x][y],fill="#2288FF")
                            Ecran_Ennemi.itemconfig(Flotte_Ennemie[x][y],fill="#2288FF")
                sous_tour+=1
                Reconnaissance="NON"
                if tour==1 :
                    Avion_utilise_J1="OUI"
                    Ecran_J1.unbind("<Motion>")
                else :
                    Avion_utilise_J2="OUI"
                    Ecran_J2.unbind("<Motion>")
            else:
               if xBis!=x or yBis!=y or evt.num==1 or evt.num==3:#Regarde si il est nÃ©cÃ©ssaire de placer un nouveau spectre de reconnaissance
                   if x<=11 and y<=11:
                        for o in range(12):
                            for v in range(12):
                                if Ecran.itemcget((Carte[o][v]),"fill")=="#DDDDDD":
                                    Ecran.itemconfig(Carte[o][v],fill="#0040FF")
                        else :
                            for t in range(12):
                                if Ecran.itemcget((Carte[x*c+b*t][y*b+c*t]),"fill")!="red" and Ecran.itemcget((Carte[x*c+b*t][y*b+c*t]),"fill")!="white":
                                    Ecran.itemconfig(Carte[x*c+b*t][y*b+c*t],fill="#DDDDDD")
                        xBis=x
                        yBis=y
    elif Missile=="OUI" and sous_tour<1 and Fin=="NON": #Partie "Missilde de croisiÃ¨re"
        a=Ecran.find_withtag(CURRENT)
        if Carte_str in Ecran.gettags(a):
            x1,y1=CoordonneesXY(evt,a ,Flotte_str, Carte_str, Ecran)
            if evt.num==1 or evt.num==2 or evt.num==3:
                for i in range(3):
                    x=x1-i+1
                    y=y1
                    if x>=0 and y>=0 and x<12 and y<12 :
                        d=Ecran_Ennemi.find_withtag(Flotte_Ennemie[x][y])
                        if "Bateau" in Ecran_Ennemi.gettags(d):
                            if Ecran.itemcget((Carte[x][y]),"fill")!="red":
                                Ecran.itemconfig(Carte[x][y],fill="red")
                                Ecran_Ennemi.itemconfig(Flotte_Ennemie[x][y],fill="red")
                                if tour==1:
                                    Points_J1+=1
                                else :
                                    Points_J2+=1
                                if Points_J1==19 or Points_J2==19:
                                    Fin="OUI"
                                    TourSuivant() 
                        else :
                            Ecran.itemconfig(Carte[x][y],fill="white")
                            Ecran_Ennemi.itemconfig(Flotte_Ennemie[x][y],fill="white")
                for h in range(3):
                    x=x1
                    y=y1-h+1
                    if x>=0 and y>=0 and x<12 and y<12 :
                        d=Ecran_Ennemi.find_withtag(Flotte_Ennemie[x][y])
                        if "Bateau" in Ecran_Ennemi.gettags(d):
                            if Ecran.itemcget((Carte[x][y]),"fill")!="red":
                                Ecran.itemconfig(Carte[x][y],fill="red")
                                Ecran_Ennemi.itemconfig(Flotte_Ennemie[x][y],fill="red")
                                if tour==1:
                                    Points_J1+=1
                                else :
                                    Points_J2+=1
                                if Points_J1==19 or Points_J2==19:
                                    Fin="OUI"
                                    TourSuivant() 
                        else :
                            Ecran.itemconfig(Carte[x][y],fill="white")
                            Ecran_Ennemi.itemconfig(Flotte_Ennemie[x][y],fill="white")
                sous_tour+=1
                Missile="NON"
                if tour==1 :
                    Missile_utilise_J1="OUI"
                else :
                    Missile_utilise_J2="OUI"
            else:
                Missile=="OUI"

def InfoPlacement():
    showinfo ("Aide au placement des bateaux","Les bateaux se placent sur la carte en haut Ã  gauche, qui plus tard montrera les actions de l'adversaire. Lorsque vous passez le curseur sur une case, un spectre vous aidera Ã  visualiser la future position du bateau, lorsque la position vous convient, cliquez avec la molette pour placer le bateau Ã  l'endroit du spectre. Pour changer l'orientation du bateau, cliquez avec le clic gauche pour placer le bateau horizontalement ou le clic droit pour placer le bateau verticallement. L'ordre des bateaux est: Porte avion (5 cases), Cuirass (4 cases), Destroyer 1 (3 cases), Destroyer 2 (3 cases), Sous-marin (2 cases), Croiseur (2 cases)") 

def InfoRecon():
    showinfo ("Utilisation de l'avion de reconnaissance","SÃ©lectionnez l'avion de reconnaissance en cliquant sur \"Envoyer un avion de reconnaissance\", ensuite, tout comme le placement de bateaux, utiliser le clic gauche pour envoyer l'avion horizontalement ou le clic droit pour l'envoyer verticalement puis le clic de la molette pour l'envoyer. L'avion rÃ©vÃ¨lera alors la ligne ou colonne de la flotte adverse.")

def InfoMissile():
    showinfo ("Utilisation du missile de croisiÃ¨re","SÃ©lectionnez le missile de croisiÃ¨re en cliquant sur \"Envoyer un missile de croisiÃ¨re\", ensuite cliquez sur la case oÃ¹ vous voulez envoyer le missile. L'explosion du missile touchera alors les 4 cases adjacentes (ou moins si le missile est envoyÃ© en bord de carte).")
        # Boutons et label 

Ecran_J1=Canvas(Fenetre, width=700, height=700, bg='#002277',bd=8,relief="ridge")
Ecran_J2=Canvas(Fenetre, width=700, height=700, bg='#772200',bd=8,relief="ridge")
Bouton_tour_suivant=Button(Fenetre, text="Tour suivant", command=TourSuivant)
Bouton_quitter=Button(Fenetre,bg="#FF5500", text="Quitter", command=Fenetre.destroy)
Bouton_InfoPlacement=Button(Fenetre,bg="#FFFFFF", text="Aide au placement des bateaux", command=InfoPlacement)
Bouton_Reconnaissance=Button(Fenetre, bg="#13A063", text="Envoyer un avion de reconnaissance", command=Reconnaissance)
Bouton_InfoRecon=Button(Fenetre, bg="#FFFFFF", text="Info", command=InfoRecon)
Bouton_Missile=Button(Fenetre, bg="#A06313",text="Envoyer un missile de croisiÃ¨re",command=Missile)
Bouton_InfoMissile=Button(Fenetre, bg="#FFFFFF",text="Info",command=InfoMissile)

Ecran_J1.pack(side=LEFT)
Bouton_tour_suivant.place(x=20,y=500)
Bouton_quitter.pack(side=RIGHT)
Bouton_InfoPlacement.place(x=300,y=100)
Bouton_Reconnaissance.place(x=20,y=300)
Bouton_InfoRecon.place(x=230,y=300)
Bouton_Missile.place(x=20,y=330)
Bouton_InfoMissile.place (x=200,y=330)

init()
Fenetre.mainloop()
