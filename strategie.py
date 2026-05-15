import diamantF as df




class ktourStrategy:
    def __init__(self):
        pass
    def play(self,
             mon_coffre, # liste d'entiers de taille nb_manches
             mon_sac, # entier : nombre de rubis
             rubis_au_sol, # rubis restants à partager
             id_manche, # entier : compris entre 1 et 5
             les_joueurs,    # [ {"coffre":[2,5,0,0,0], "is_active" : True}
                             #,... ,
                             # {"coffre": [0,15,3,0,0], "is_active" : False} ]
             tas_tri, # le tas de cartes restantes (pas dans l'ordre de tirage)
             defausse # ce qui est déjà joué comme cartes
            ):
         return len(defausse) > 4
     
     
     
class strategie_test1:
    def __init__(self):
        pass
    def chill(self , mon_coffre , mon_sac , rubis_au_sol  , id_manche , les_joueurs , tas_tri , defausse):
        if mon_sac >= 10 or df.compte_nb_piege(defausse)>=2 :
            return False
        else: 
            return True

    def ambitieux(self , mon_coffre , mon_sac , rubis_au_sol  , id_manche , les_joueurs , tas_tri , defausse):
        if len(defausse) < 8 :
            return True
        else : 
            return False
    
    def suis(self , mon_coffre , mon_sac , rubis_au_sol  , id_manche , les_joueurs , tas_tri , defausse):
        if df.nombre_joueurs_sorti(les_joueurs)==len(les_joueurs)//2:
            return False
        else: 
            return True


class strat_abs :
    def __init__(self):
        pass
    def play(self,
        mon_coffre, # liste d'entiers de taille nb_manches
        mon_sac, # entier : nombre de rubis
        rubis_au_sol, # rubis restants à partager
        id_manche, # entier : compris entre 1 et 5
        les_joueurs,    # [ {"coffre":[2,5,0,0,0], "is_active" : True}
                             #,... ,
                             # {"coffre": [0,15,3,0,0], "is_active" : False} ]
        tas_tri, # le tas de cartes restantes (pas dans l'ordre de tirage)
        defausse, # ce qui est déjà joué comme cartes
        relique_de_cote,
        nb_joueurs_actif
            ):
        if df.prise_risque(les_joueurs , mon_coffre , id_manche)==True:
            if df.proba_mort <0.3:
            
                nb_joueurs_sort=df.estimation_sorti_joueurs(les_joueurs ,defausse ,id_manche , rubis_au_sol , relique_de_cote ,nb_joueurs_actif)
            
                if df.calcul_gain_possible(mon_sac , rubis_au_sol , relique_de_cote , nb_joueurs_sort) >= 25 :
                    return False
                else: 
                    return True
            else : 
                return False
        else:
            if df.proba_mort(defausse , tas_tri) <0.6:
            
                nb_joueurs_sort=df.estimation_sorti_joueurs(les_joueurs ,defausse ,id_manche , rubis_au_sol , relique_de_cote ,nb_joueurs_actif)
            
                if df.calcul_gain_possible(mon_sac , rubis_au_sol , relique_de_cote , nb_joueurs_sort) >= 17 :
                    return False
                else: 
                    return True
            else : 
                return False