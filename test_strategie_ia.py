import diamantF as df


printing=False
nb_joueurs_total=3

point_strat={"chill" : 0 , "ambitieux" : 0 , "suis" : 0}
strat=["chill" , "ambitieux" , "suis"]
carte_jeu=df.cartes.copy()
joueurs=[]
for i in range(nb_joueurs_total):
    
    if printing == True :
        #on met le nom dans une liste
        
        nom=input(f"rentrer le nom du joueur {i+1} : ")
        
        #on ajoute le nom dans la liste de dictionnaires
        
        dic={"nom":nom ,"coffre":[0,0,0,0,0], "is_active" : True , "sac":0 , "strat" : strat[i] }
    else:  

        dic={"nom":f"IA{i+1}" ,"coffre":[0,0,0,0,0], "is_active" : True , "sac":0 , "strat" : strat[i] }
    joueurs.append(dic)



print("-----------------------------------LA PARTIE COMMENCE---------------------")
for p in range(0,10000):
    for j in joueurs:
        j["coffre"] = [0, 0, 0, 0, 0]
        j["sac"] = 0
        j["is_active"] = True
        
    carte_jeu.clear()
    carte_jeu=df.cartes.copy()
    
    for i in range(1,6):
        
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


        while(piege_double==False and joueurs_active==True and len(carte_jeu) > 0):
            # on remet la liste de joueurs sorti vide

            joueurs_sorti.clear()


            # tirage de la carte 

            carte_tirer=df.tire_carte(carte_jeu)
            defausse.append(carte_tirer)

            #on retire la carte tirer du jeu

            carte_jeu.pop(0)
            
        
                
        
        

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
                    
                else :
                    piege.append(carte_tirer)
                

        
        
            if piege_double == False :
                
                nb_joueur=df.continu_strat(joueurs , nb_joueur , joueurs_sorti , rubis_au_sol , i-1 ,carte_jeu , defausse)
                

                    


                # distribution des points de reliques si sorti  

                df.distribution_relique(joueurs_sorti ,  relique_de_cote , joueurs , i , defausse)  # i cest le numero de manche
            

                # distribution des rubis au sol 
                df.distribution_des_rubis_au_sol(joueurs , joueurs_sorti  ,rubis_au_sol)
            
    
            
            # ce if determine si tout les joueurs sont sorti ou pas
            if df.tous_sorti(joueurs)==True :
                joueurs_active=False
            
            # on met le contenu du sac dans le coffre si le joueur est sorti
            df.transfere_sac_coffre(joueurs , joueurs_sorti , i)
        df.remettre_carte(carte_jeu , defausse)
        
    if df.design_gagnant(joueurs)[3]=="chill" :
        point_strat["chill"]+=1
    elif df.design_gagnant(joueurs)[3]=="ambitieux" :
        point_strat["ambitieux"]+=1
    else:
        point_strat["suis"]+=1


for j in range(len(point_strat)):
    print(point_strat)
    
    
        


    