import diamantF as df 

#on defini ici le nombre de joueurs

nb_joueurs_total=int(input("Combien de joueurs veulent rentrer dans la grotte? "))

# on stock le nom des joueurs 
joueurs=[]

for i in range(nb_joueurs_total):
    #on met le nom dans une liste

    nom=input(f"rentrer le nom du joueur {i+1} : ")

    #on ajoute le nom dans la liste de dictionnaires

    dic={"nom":nom ,"coffre":[0,0,0,0,0], "is_active" : True , "sac":0 }
    joueurs.append(dic)
    

# lot de cartes de jeu 
carte_jeu=df.cartes.copy()

# on commence le jeu 
print("-----------------------------------LA PARTIE COMMENCE---------------------")
for i in range(1,6):
    print(f"\n---------------------------LA MANCHE {i} COMMENCE---------------------- ")

    # On ajoute la relique au cartes

    carte_jeu.append(df.reliques[i-1])


    piege_double=False
    joueurs_active=True
    defausse=[]
    rubis_au_sol=[0]
    relique_de_cote=[]
    piege=[]
    joueurs_sorti=[]


    # variale qui stock le nombre de joueurs total pour pouvoir la manipuler librement chaque manche

    nb_joueur=nb_joueurs_total


    while(piege_double==False and joueurs_active==True ):
        # on remet la liste de joueurs sorti vide

        joueurs_sorti=[]


        # tirage de la carte 

        carte_tirer=df.tire_carte(carte_jeu)
        defausse.append(carte_tirer)

        #on retire la carte tirer du jeu

        carte_jeu.pop(0)
        
        print(f"----Voici la carte qui a été tirer : {carte_tirer} \n")
        

        if carte_tirer in  df.rubis_jeu :

            # distribution des rubis en cas de carte rubis tiré
            df.rubis(carte_tirer , nb_joueur ,rubis_au_sol ,joueurs , i-1 )

        elif carte_tirer in df.reliques :

            
            relique_de_cote.append(carte_tirer)

        else:
            # dans ce if on voit si le piege sorti est deja sorti si cest le cas on enleve tous les rubis du sac des joueurs actifs sinon on lajoute a piege
            if carte_tirer in piege :
                for j in joueurs : 
                    j["sac"]=0
                piege_double=True
                print()
            else :
                piege.append(carte_tirer)
                

        
        
        if piege_double == False :

            # la decision des joueurs continuer ou revenir vers la grotte
            if len(defausse)>=1 :
                print(f"----------Voici les cartes qui sont sorti : {defausse}  PENSEZ BIEN AVANT D'AGIR!!!! \n")
            nb_joueur=df.continu(joueurs,nb_joueur,joueurs_sorti)
            print(nb_joueur)

                    


            # distribution des points de reliques si sorti  

            df.distribution_relique(joueurs_sorti ,  relique_de_cote , joueurs , i , defausse)  # i cest le numero de manche
            

            # distribution des rubis au sol 
            df.distribution_des_rubis_au_sol(joueurs , joueurs_sorti  ,rubis_au_sol)
            
    
            
        # ce if determine si tout les joueurs sont sorti ou pas
        if df.tous_sorti(joueurs)==True :
            joueurs_active=False
            
        # on met le contenu du sac dans le coffre si le joueur est sorti
        df.transfere_sac_coffre(joueurs , joueurs_sorti , i)
        
    print("voici le contenu de vos coffre : ")
    # on affiche les coffres de tout les joueurs et on remet tout les joueurs actif

    df.affiche_coffre(joueurs)

    # on remet les cartes rubis  qui on été utiliser durant une manche et les reliques non utiliser dans le lot
    
    df.remettre_carte(carte_jeu , defausse)
    
    
print("-------------------------------LA DERNIERE MANCHE EST TERMINÉ-----------------------------------")


if df.design_gagnant(joueurs)[2] != nb_joueurs_total:
    print(f"\nLE GAGNANT DE LA PARTIE EST  :  {df.design_gagnant(joueurs)[0]} AVEC UN TOTAL DE {df.design_gagnant(joueurs)[1]} POINTS !!!!!")
else:
    print("\n--------TOUT LES JOUEURS ONT LES MEMES POINTS-----------------")
    print("----------------PERSONNE N'A GAGNÉ----------------------------")
    
print("\n-------------LA PARTIE EST TERMINÉ!!!!!!!!!!!!!!!------------- ")

 


