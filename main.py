import argparse


def analyser_commande():
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = "Jeux Quoridor - phase 1")
    
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument('idul', help = 'IDUL du joueur.')
    parser.add_argument('-l', '--lister', help = 'Lister les identifiants de vos 20 dernières parties', action = 'store_true')
    return parser.parse_args()





analyser_commande()