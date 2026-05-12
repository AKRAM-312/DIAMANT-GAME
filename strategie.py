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