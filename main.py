"""Ceci est mon main"""
import argparse
import api


def analyser_commande():
    """Ceci est mon analyseur"""
    # créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser(description="Jeux Quoridor - phase 1")
    # insérer ici avec les bons appels à la méthode add_argument
    parser.add_argument('idul', help='IDUL du joueur.')
    temp = 'Lister les identifiants de vos 20 dernières parties'
    parser.add_argument('-l', '--lister', dest='lister', help=temp, action='store_true')
    return parser.parse_args()

def afficher_damier_ascii(dico):
    """Ceci affiche mon damier"""
    tabmv = [[' 'for i in range(8)]for i in range(17)]
    tabmh = [[' 'for i in range(35)]for i in range(8)]
    tabj = [['.'for i in range(9)]for i in range(9)]
    for i in dico['joueurs']:
        if i['nom'] == 'robot':
            tabj[9-(i['pos'][1])][(i['pos'][0])-1] = '2'
        else:
            tabj[9-(i['pos'][1])][(i['pos'][0])-1] = '1'
    for i in dico['murs']['verticaux']:
        tabmv[int(17-(i[1]*2)+1)][i[0]-2] = '|'
        tabmv[int(17-(i[1]*2))][i[0]-2] = '|'
        tabmv[int(17-(i[1]*2)-1)][i[0]-2] = '|'
    for i in dico['murs']['horizontaux']:
        for b in range(7):
            tabmh[9-i[1]][int(i[0]*4)-4+b] = '-'
    counter = 18
    print(f'Légende: 1={dico["joueurs"][0]["nom"]}, 2=robot')
    print(' ' * 3 + '-' * 35)
    for i in range(17):
        a = ""
        if i % 2 == 0:
            for j in range(36):
                if j == 0:
                    a += f"{str(int(counter/2))} |"
                elif j % 2 == 1:
                    a += ' '
                elif (j+2) % 4 == 0:
                    a += tabj[int(i/2)][int((j-1)/4)]
                else:
                    a += tabmv[i][int(j/4)-1]
        else:
            a = '  |'
            for j in range(35):
                if (j-3) % 4 == 0 and tabmv[i][int((j-3)/4)] != ' ':
                    a += tabmv[i][int((j-3)/4)]
                else:
                    a += tabmh[int((i-1)/2)][j]
        print(f"{a}|")
        counter -= 1
    print('--|' + '-'*35)
    print('  | 1   2   3   4   5   6   7   8   9')

def getpos():
    """Ceci me permet de demander a mon utilisateur d'entrer un position valide"""
    ok2 = False
    print('Entrez la position où vous voulez vous déplacer')
    print("Vos données doivent être entre 0 et 9 et séparées d'une virgule")
    while not ok2:
        pos = ()
        choix1 = input()
        po = str(choix1).split(',')
        if len(po) == 2:
            if po[0].isdigit() and po[1].isdigit():
                pos = (int(po[0]), int(po[1]))
                if (pos[0] < 10 and pos[0] >= 0) and (pos[1] < 10 and pos[1] >= 0):
                    ok2 = True
                else:
                    print('Données invalides   ex: 2,3')
            else:
                print('INVALIDE -Entrez seulement des chiffres   ex: 2,3')
        else:
            print('INVALIDE -Entrez exactement 2 données   ex: 2,3')
    return pos

GAMEDONE = False
AN = analyser_commande()
if AN.lister:
    print(api.lister_parties(AN.idul))
else:
    IDGAME, STATE = api.débuter_partie(AN.idul)
    while not GAMEDONE:
        afficher_damier_ascii(STATE)
        try:
            print('\n\n\nChoisissez une option parmi les suivantes:')
            print('\n1- Déplacer son joueur')
            print('2- Placer un mur horizontal')
            print('3- Placer un mur vertical')
            print('4- Quitter')
            OK = False
            while not OK:
                CHOIX = input()
                if str(CHOIX) == '1':
                    OK = True
                    POS = getpos()
                    STATE = api.jouer_coup(IDGAME, 'D', POS)
                elif str(CHOIX) == '2':
                    POS = getpos()
                    STATE = api.jouer_coup(IDGAME, 'MH', POS)
                    OK = True
                elif str(CHOIX) == '3':
                    POS = getpos()
                    STATE = api.jouer_coup(IDGAME, 'MV', POS)
                    OK = True
                elif str(CHOIX) == '4':
                    OK = True
                    GAMEDONE = True
                    print('BYE BYE!!')
                else:
                    print('Le  choix rentré est invalide')
        except RuntimeError as err:
            print(f'\n{str(err)}\n')
        except StopIteration as err:
            print(f'\nLe joueur {str(err)} a remporté la partie!!\n')
            GAMEDONE = True
