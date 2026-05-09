import random
cartes = ["1", "2", "3", "4", "5", "5", "7", "7", "9", "11", "11", "13", "14", "15", "17", 
                "serpents", "boulets", "pics", "araignées", "lave",
                "serpents", "boulets", "pics", "araignées", "lave",
                "serpents", "boulets", "pics", "araignées", "lave"]

reliques = ["R_5","R_7","R_8","R_10","R_12"]

rubis_jeu=["1", "2", "3", "4", "5", "5", "7", "9","11", "13", "14", "15", "17"] 





# fonction qui tire une carte aleatoirement

def tire_carte(cartes):
    random.shuffle(cartes)
    return cartes[0]

# fonction qui permet de retirer la carte du jeu 

def retire(cartes , carte_a_retirer ):
    cartes.remove(carte_a_retirer)

# fonction qui determine si les joueurs tous sorti ou pas

def tous_sorti (joueurs):
    nb=0
    for i in joueurs :
        if i["is_active"]==False:
            nb+=1
    if nb==len(joueurs):
        return True
    else : 
        return False

# fonction qui distribu les rubis equitablement 

def rubis (cartes_tirer , nb_joueurs , rubis_au_sol,joueurs ,nb_manche):

    # on voit si le nombre de rubis est inferieur au nombre de joueur si cest le cas on les laisse au sol 
    if int(cartes_tirer) < int(nb_joueurs) :
        rubis_au_sol[0]+=int(cartes_tirer)
        rubis_a_partager=0
    else:

        # la on met le reste des rubis au sol grace au mod
        rubis_au_sol[0]+=( int(cartes_tirer) % int(nb_joueurs) )
        
        # et la on stock le nombre de rubis qui seront partager 
        rubis_a_partager=  int(cartes_tirer)//int(nb_joueurs)

    for i in joueurs : 
        i["sac"]+=rubis_a_partager

# fonction  qui demande aux joueurs qui sont en pleine expedition si ils veulent retourner ou pas a la grotte
def continu(joueurs ,nb_joueur , joueur_sorti):
    for i in range(len(joueurs)):
        if joueurs[i]["is_active"]==True: 
            continu=input(f"{joueurs[i]['nom']} voulez vous continuer lexpedition ? ")

            if continu == "non" or continu == "Non" or continu == "No" or continu=="no" :
                joueur_sorti.append(joueurs[i])
                joueurs[i]["is_active"]=False
                nb_joueur-=1
                print(f"{joueurs[i]['nom']} sort de l'éxpédition")
    return nb_joueur

def piege_double(carte_tirer , piege, joueurs , nb_manche):
    if carte_tirer in piege :
        for i in joueurs : 
            if i["is_active"]==True :
                i["coffre"][nb_manche]=0

# fonction qui determine si un seul joueur est sorti durant la manche
def un_joueur_sorti(joueurs_sorti ):
    if len(joueurs_sorti)==1:
        return True 
    else:
        return False
    
def affiche_coffre (joueurs):
    for j in range(len(joueurs)) :
        print(joueurs[j]["nom"] , " : ",joueurs[j]["coffre"] )
        joueurs[j]["is_active"]=True
        joueurs[j]["sac"]=0

def remettre_carte(carte_jeu , defausse):
    for j in defausse:
        if j.lstrip('-').isdigit()  or j in reliques:
            carte_jeu.append(j)

def transfere_sac_coffre(joueurs , joueurs_sorti , nb_manche):
    for j in range(len(joueurs)):
            if joueurs[j]["is_active"]==False:
                joueurs[j]["coffre"][nb_manche-1]+=joueurs[j]["sac"]
                

def distribution_relique(joueurs_sorti , relique_de_cote , joueurs , num_manche ,defausse ):
    if  un_joueur_sorti(joueurs_sorti)==True and len(relique_de_cote)>=1 :
            for j in range(len(relique_de_cote)):
                for k in joueurs:
                    if k["nom"]==joueurs_sorti[0]["nom"] :
                        if len(relique_de_cote[j])== 3:
                            k["coffre"][num_manche-1]+=int(relique_de_cote[j][2])
                        else:
                            k["coffre"][num_manche-1]+= ( int(relique_de_cote[j][2])*10 + int(relique_de_cote[j][3]) )
                # on enleve la carte relique de la defausse puisqu'elle a etait deja utiliser et pour quelle soit pas utiliser dans les manches suivantes
                defausse.remove(relique_de_cote[j])
            


def distribution_des_rubis_au_sol(joueurs , joueurs_sorti   , rubis_au_sol ):
    if len(joueurs_sorti)>0:
        for j in joueurs:
            if j in joueurs_sorti:
                j["sac"]+=rubis_au_sol[0] // len(joueurs_sorti)
        rubis_au_sol[0] = rubis_au_sol[0] % len(joueurs_sorti)
        print(f"il reste {rubis_au_sol[0]} rubis au sol")   


def design_gagnant(joueurs):
    max_point=0
    for i in joueurs :
       if sum(i["coffre"])>max:
           max_point=sum(i["coffre"])
           nom_gagnant=i["nom"]
    return nom_gagnant , max 
           